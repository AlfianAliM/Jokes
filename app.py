import os
import replicate
from dotenv import load_dotenv

# Memuat token dari file .env
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

if not REPLICATE_API_TOKEN:
    raise ValueError("Token API Replicate tidak ditemukan. Pastikan file .env sudah benar.")

# Set API Token untuk Replicate
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

# Fungsi untuk menghasilkan tebak-tebakan
def generate_joke_stream():
    try:
        print("Mengirim prompt ke Replicate...")

        # The meta/meta-llama-3-8b-instruct model can stream output as it's running.
        for event in replicate.stream(
            "meta/meta-llama-3-8b-instruct",
            input={
                "top_k": 0,
                "top_p": 0.95,
                "prompt": "Buatkan jokes bahasa indonesia seperti ini contohnya \n\n\"Apa persamaan antara uang dan rahasia?\n\nSama-sama susah dipegang 😔😔\"",
                "max_tokens": 512,
                "temperature": 0.7,
                "system_prompt": "You are a helpful assistant",
                "length_penalty": 1,
                "max_new_tokens": 512,
                "stop_sequences": "<|end_of_text|>,<|eot_id|>",
                "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
                "presence_penalty": 0,
                "log_performance_metrics": False,
            },
        ):
            print(str(event), end="")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Memanggil fungsi
generate_joke_stream()
