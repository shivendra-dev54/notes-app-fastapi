
import { useState } from "react";
import { useNavigate } from "react-router";
import { request } from "../utils/requestHandler";
import { useAuthStore } from "../lib/AuthStore";

export default function SignInPage() {
	const { setUser } = useAuthStore();
	const navigate = useNavigate();

	const [form, setForm] = useState({ email: "", password: "" });

	const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		setForm({ ...form, [e.target.name]: e.target.value });
	};

	const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		const res = await request(
			"/user/sign_in",
			{
				'email': form.email,
				'password': form.password
			},
			"POST"
		);
		const data = await res.json();

		if(data.success){
			setUser(data.data);
			navigate("/main");
		}
	};

	return (
		<div className="min-h-content mt-40 bg-black text-white flex items-center justify-center px-6">
			<form
				onSubmit={async (e: React.FormEvent<HTMLFormElement>) => await handleSubmit(e)}
				className="w-full max-w-md bg-gray-900 p-8 rounded-lg border border-gray-800"
			>
				<h2 className="text-2xl font-bold mb-6 text-center">Sign In</h2>

				<input
					type="email"
					name="email"
					placeholder="Email"
					value={form.email}
					onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleChange(e)}
					className="w-full p-3 mb-4 bg-black border border-gray-700 rounded text-white"
				/>
				<input
					type="password"
					name="password"
					placeholder="Password"
					value={form.password}
					onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleChange(e)}
					className="w-full p-3 mb-6 bg-black border border-gray-700 rounded text-white"
				/>

				<button
					type="submit"
					className="w-full p-3 bg-gray-800 hover:bg-gray-700 rounded text-white"
				>
					Sign In
				</button>
			</form>
		</div>
	);
}
