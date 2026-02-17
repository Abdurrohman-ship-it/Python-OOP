class Hero:
    # --- TUGAS 2: MUSUH & TIPE KARAKTER & TUGAS 1: PARTY HERO ---
    # Constructor menerima parameter untuk inisialisasi object
    def __init__(self, name, role, hp, char_type="hero"):
        self.name = name
        self.role = role
        self.hp = hp
        self.max_hp = hp  # Menyimpan Max HP untuk batas Heal dan Logic Boss
        self.type = char_type # "hero", "normal", atau "boss"
        
        print(f"✨ {self.name} [{self.role}] memasuki arena! (HP: {self.hp})")

    # Helper method untuk cek status hidup
    def is_alive(self):
        return self.hp > 0

    # Method untuk menyerang
    def attack(self, enemy, damage):
        # --- TUGAS 3: ATURAN HIDUP & MATI (Cek Penyerang) ---
        if not self.is_alive():
            print(f"🚫 {self.name} sudah mati, tidak bisa menyerang!")
            return

        # Cek jika target sudah mati
        if not enemy.is_alive():
            print(f"⚠️ {enemy.name} sudah mati, tidak perlu diserang lagi.")
            return
        
        # Validasi damage tidak boleh negatif
        if damage <= 0:
            print("❌ Damage tidak valid!")
            return

        final_damage = damage

        # --- TUGAS 4: ROLE HERO (Mage Damage Bonus) ---
        if self.role == "Mage":
            print(f"⚡ {self.name} memusatkan energi sihir! (Bonus Damage)")
            final_damage += 20 

        # --- TUGAS 5: BOSS MODE (RAGE MODE) ---
        # Jika tipe Boss DAN HP kurang dari atau sama dengan 50%
        if self.type == "boss" and self.hp <= (self.max_hp * 0.5):
            print(f"\n😈 {self.name} memasuki RAGE MODE!")
            print("🔥 AURA GELAP MENYELIMUTI RAJA IBLIS! (CRITICAL HIT)")
            final_damage = final_damage * 2 # Damage dikali 2
        
        print(f"⚔️ {self.name} menyerang {enemy.name} dengan kekuatan {final_damage}!")
        
        # Panggil method take_damage milik musuh
        enemy.take_damage(final_damage)

    # Method untuk menerima damage
    def take_damage(self, damage):
        self.hp -= damage
        
        # --- TUGAS 3: ATURAN HIDUP & MATI (Cek HP limit) ---
        if self.hp < 0:
            self.hp = 0
            
        print(f"   🤕 {self.name} terkena {damage} dmg. Sisa HP: {self.hp}/{self.max_hp}")

        if self.hp == 0:
            print(f"   💀 {self.name} telah GUGUR!")

    # Method untuk heal
    def heal(self, amount):
        # Cek apakah karakter masih hidup
        if not self.is_alive():
            print(f"🚫 {self.name} sudah mati, tidak bisa dipulihkan.")
            return

        # --- TUGAS 4: ROLE HERO (Healer Bonus) ---
        if self.role == "Healer":
            print(f"✨ {self.name} menggunakan Blessing! (Heal Boost)")
            amount += 20 # Bonus heal

        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"💚 {self.name} dipulihkan sebanyak {amount}. HP sekarang: {self.hp}/{self.max_hp}")

# --- SETUP (DATA UJI MINIMAL) ---
print("\n=== PERSIAPAN PARTY ===")
hero1 = Hero("Zilong", "Warrior", 120, "hero")  # HP Besar (Warrior)
hero2 = Hero("Eudora", "Mage", 80, "hero")      # HP Kecil, Damage Besar (Mage)
hero3 = Hero("Rafaela", "Healer", 70, "hero")   # HP Kecil, Heal Besar (Healer)

print("\n=== MUSUH MUNCUL ===")
goblin = Hero("Goblin", "Normal", 50, "normal")
boss = Hero("Raja Iblis", "Boss", 200, "boss")  # Boss dengan HP 200

# --- SIMULASI PERTARUNGAN (MANUAL) ---

print("\n\n⚔️ --- RONDE 1: VS GOBLIN --- ⚔️")
hero1.attack(goblin, 30)
goblin.take_damage(20) # Manual call attack dari goblin ke hero
hero2.attack(goblin, 40) # Mage attack + bonus = One Shot

print("\n\n⚔️ --- RONDE 2: VS BOSS (RAJA IBLIS) --- ⚔️")
boss.attack(hero1, 20)
hero3.heal(20) # Heal hero1

print("\n--- SERANGAN PARTAI HERO KE BOSS ---")
hero1.attack(boss, 50) # HP Boss sisa 150
hero2.attack(boss, 60) # HP Boss sisa 90 (50 base + 20 bonus mage = 70 dmg, 90 HP left)

print("\n--- BOSS MASIH KUAT ---")
boss.attack(hero3, 50) # Boss attack normal

print("\n--- BOSS MULAI KRITIS ---")
hero1.attack(boss, 40) # HP Boss sisa 50 (Tepat 50%!)

print("\n\n⚠️ --- RONDE 3: BOSS RAGE MODE --- ⚠️")
# Saat HP Boss <= 50%, serangan Boss menjadi CRITICAL (Double Damage)
boss.attack(hero2, 60) # Damage 60 * 2 = 120 (Eudora HP 80, mati!)

print("\n--- COBA AKSI DARI KARAKTER MATI ---")
hero2.attack(boss, 10) # Seharusnya gagal karena Eudora sudah mati
hero2.heal(50)         # Seharusnya gagal

print("\n=== PERTARUNGAN SELESAI ===")