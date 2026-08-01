import os
current_stage = os.getenv("STAGE", "development")

print("\n--- ЗАПУСК ПРИЛОЖЕНИЯ ---")
if current_stage == "production":
    print("🔒 БЕЗОПАСНОСТЬ: Режим Production. База реальная.")
else:
    print("🛠️ РЕЖИМ РАЗРАБОТКИ: Режим Development. База тестовая.")
