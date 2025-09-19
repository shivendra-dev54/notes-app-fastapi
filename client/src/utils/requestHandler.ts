import { useAuthStore } from "../lib/AuthStore";

const API_BASE = "http://localhost:8000/api/v0";

async function refreshToken() {
  try {
    const res = await fetch(`${API_BASE}/user/refresh`, {
      method: "PUT",
      credentials: "include",
    });

    if (!res.ok) throw new Error("Refresh failed");
    return true;
  } catch (err) {
    console.error("Refresh error:", err);
    useAuthStore.getState().logout();
    return false;
  }
}

export async function request(
  endpoint: string,
  body?: object,
  method: string = "GET",
  retry = true
) {
  try {
    const fetchOptions: RequestInit = {
      method,
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    };

    if (body && method !== "GET") {
      fetchOptions.body = JSON.stringify(body);
    }

    const res = await fetch(`${API_BASE}${endpoint}`, fetchOptions);

    if (res.status === 401 && retry) {
      const refreshed = await refreshToken();
      if (refreshed) {
        return request(endpoint, body, method, false);
      }
    }

    return res;
  } catch (err) {
    console.error("Request error:", err);
    throw err;
  }
}
