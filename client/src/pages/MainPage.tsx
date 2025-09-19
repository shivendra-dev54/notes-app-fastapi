import { useCallback, useEffect, useState } from "react";
import { useAuthStore } from "../lib/AuthStore";
import { request } from "../utils/requestHandler";
import { useNavigate } from "react-router";

export default function MainPage() {
	const { user, logout } = useAuthStore();
	const [notes, setNotes] = useState<{ id: number; content: string }[]>([]);
	const [newNote, setNewNote] = useState("");
	const [editingNoteId, setEditingNoteId] = useState<number | null>(null);
	const [editContent, setEditContent] = useState("");

	const navigate = useNavigate();

	const fetchNotes = async () => {
		const res = await request("/note/read", {}, "GET");
		const data = await res.json();
		if (data?.success) setNotes(data.data);
	};

	const addNote = async () => {
		if (!newNote.trim()) return;
		const res = await request("/note/create", { content: newNote }, "POST");
		const data = await res.json();
		if (data.success) {
			setNewNote("");
			fetchNotes();
		}
	};

	const deleteNote = async (id: number) => {
		await request(`/note/delete/${id}`, {}, "DELETE");
		fetchNotes();
	};

	const startEditing = (id: number, content: string) => {
		setEditingNoteId(id);
		setEditContent(content);
	};

	const cancelEditing = () => {
		setEditingNoteId(null);
		setEditContent("");
	};

	const updateNote = async (id: number) => {
		if (!editContent.trim()) return;
		const res = await request(`/note/update/${id}`, { content: editContent }, "PUT");
		const data = await res.json();
		if (data.success) {
			setEditingNoteId(null);
			setEditContent("");
			fetchNotes();
		}
	};

	const logout_handler = async () => {
		const res = await request("/user/logout", {}, "POST");
		const data = await res.json();
		if (data) {
			logout();
		}
	};

	const check_user_status = useCallback(async () => {
		if (!user) {
			logout();
			navigate("/");
		}
	}, [logout, navigate, user]);

	useEffect(() => {
		check_user_status();
		fetchNotes();
	}, [check_user_status]);

	return (
		<div className="min-h-content bg-black text-white p-6">
			<div className="max-w-2xl mx-auto">
				<h1 className="text-3xl font-bold mb-6">Your Notes</h1>

				{/* Add New Note */}
				<div className="flex gap-2 mb-6">
					<input
						type="text"
						placeholder="Write a note..."
						value={newNote}
						onChange={(e) => setNewNote(e.target.value)}
						className="flex-grow p-3 bg-black border border-gray-700 rounded text-white"
					/>
					<button
						onClick={addNote}
						className="px-4 bg-gray-800 hover:bg-gray-700 rounded"
					>
						Add
					</button>
				</div>

				{/* Notes List */}
				<ul className="space-y-3">
					{notes.map((note) => (
						<li
							key={note.id}
							className="flex justify-between items-center bg-gray-900 p-3 rounded border border-gray-800"
						>
							{editingNoteId === note.id ? (
								<div className="flex w-full gap-2">
									<input
										type="text"
										value={editContent}
										onChange={(e) => setEditContent(e.target.value)}
										className="flex-grow p-2 bg-black border border-gray-700 rounded text-white"
									/>
									<button
										onClick={() => updateNote(note.id)}
										className="px-3 bg-green-700 hover:bg-green-600 rounded"
									>
										Save
									</button>
									<button
										onClick={cancelEditing}
										className="px-3 bg-gray-700 hover:bg-gray-600 rounded"
									>
										Cancel
									</button>
								</div>
							) : (
								<>
									<span>{note.content}</span>
									<div className="flex gap-2">
										<button
											onClick={() => startEditing(note.id, note.content)}
											className="text-blue-400 hover:text-blue-200"
										>
											Edit
										</button>
										<button
											onClick={() => deleteNote(note.id)}
											className="text-red-400 hover:text-red-200"
										>
											Delete
										</button>
									</div>
								</>
							)}
						</li>
					))}
				</ul>

				{/* Logout */}
				<button
					onClick={() => logout_handler()}
					className="mt-10 w-full p-3 bg-gray-800 hover:bg-gray-700 rounded"
				>
					Logout
				</button>
			</div>
		</div>
	);
}
