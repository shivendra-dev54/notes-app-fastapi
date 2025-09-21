import { useState } from "react";
import { useNavigate } from "react-router";
import { request } from "../utils/requestHandler";

export default function SignUpPage() {
	const navigate = useNavigate();

	const [form, setForm] = useState({ username: "", email: "", password: "" });

	const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		setForm({ ...form, [e.target.name]: e.target.value });
	};

	const handleSubmit = async (e: React.FormEvent) => {
		e.preventDefault();
		const success = await request(
			'/user/sign_up',
			{
				username: form.username,
				email: form.email,
				password: form.password
			},
			'POST',
			true,
		);
		const body = await success.json()
		if (body.success) {
			navigate("/sign-in");
		}
	};

	return (
		<div className="min-h-content mt-40 bg-black text-white flex items-center justify-center px-6">
			<form
				onSubmit={(e: React.FormEvent<HTMLFormElement>) => handleSubmit(e)}
				className="w-full max-w-md bg-gray-900 p-8 rounded-lg border border-gray-800"
			>
				<h2 className="text-2xl font-bold mb-6 text-center">Sign Up</h2>

				<input
					type="text"
					name="username"
					placeholder="Username"
					value={form.username}
					onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleChange(e)}
					className="w-full p-3 mb-4 bg-black border border-gray-700 rounded text-white"
				/>
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
					Sign Up
				</button>
			</form>
		</div>
	);
}
