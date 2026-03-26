import os, asyncio, requests
from nicegui import ui, app

# Railway ne dă automat portul, noi doar îl citim
PORT = int(os.environ.get("PORT", 8080))
OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY")

async def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {"role": "system", "content": "Ești MailAI Queen, Arhitect Software Senior. Construiești un imperiu de lead generation."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        res = await asyncio.get_event_loop().run_in_executor(None, lambda: requests.post(url, headers=headers, json=data, timeout=30))
        return res.json()['choices'][0]['message']['content']
    except:
        return "Regina are o mică eroare de conexiune. Verifică cheia API!"

@ui.page('/')
def main():
    ui.query('body').style('background-color: #f8fafc;')
    with ui.column().classes('w-full items-center p-10'):
        ui.label('MailAI Swarm OS - ELITE').classes('text-4xl font-black text-blue-600')
        chat = ui.column().classes('w-full max-w-2xl border p-4 rounded-xl bg-white shadow-lg h-96 overflow-y-auto')

        async def send():
            msg = input_field.value
            input_field.value = ''
            with chat:
                ui.label(f"Master: {msg}").classes('bg-blue-100 p-2 rounded-lg self-end')
                thinking = ui.label("Regina gândește...").classes('italic text-slate-400')
                response = await ask_ai(msg)
                thinking.delete()
                ui.markdown(f"**Queen:** {response}").classes('bg-slate-100 p-2 rounded-lg')

        input_field = ui.input('Ordin pentru Regină...').classes('w-full max-w-2xl mt-4').on('keydown.enter', send)
        ui.button('TRIMITE', on_click=send).classes('bg-blue-600 text-white px-10 mt-2')

ui.run(host='0.0.0.0', port=PORT, title="MailAI Elite", reload=False, show=False)