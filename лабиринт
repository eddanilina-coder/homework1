import random

class Location:
    def __init__(self, info, key_here=False, locked=False, object_here=None):
        self.info = info
        self.key_here = key_here
        self.locked = locked
        self.object_here = object_here
        self.paths = {}
        self.was_visited = False

class Adventurer:
    def __init__(self):
        self.bag = []
        self.key_count = 0
        self.position = None

class DungeonAdventure:
    def __init__(self):
        self.adventurer = Adventurer()
        self.locations = {}
        self.build_dungeon()
        self.adventurer.position = self.locations["entrance"]
    
    def build_dungeon(self):
        # Создаем локации
        self.locations = {
            "entrance": Location("Каменный вход в подземелье. Перед вами несколько путей.", key_here=True),
            "corridor": Location("Длинный коридор. В воздухе витает пыль.", object_here="свиток"),
            "archive": Location("Комната с древними манускриптами.", locked=True),
            "vault": Location("Секретное хранилище с сокровищами.", key_here=True),
            "courtyard": Location("Заброшенный внутренний двор.", object_here="аптечка"),
            "prison": Location("Тюремные камеры. Слышны непонятные шорохи.", locked=True),
            "freedom": Location("УРА! Вы выбрались из подземелья!", key_here=True)
        }
        
        # Прокладываем маршруты
        self.locations["entrance"].paths = {"вперед": self.locations["corridor"], "право": self.locations["archive"], "лево": self.locations["courtyard"]}
        self.locations["corridor"].paths = {"назад": self.locations["entrance"], "право": self.locations["vault"]}
        self.locations["archive"].paths = {"лево": self.locations["entrance"], "вперед": self.locations["prison"]}
        self.locations["vault"].paths = {"лево": self.locations["corridor"]}
        self.locations["courtyard"].paths = {"право": self.locations["entrance"], "вперед": self.locations["freedom"]}
        self.locations["prison"].paths = {"назад": self.locations["archive"]}
        self.locations["freedom"].paths = {"назад": self.locations["courtyard"]}
    
    def show_location(self):
        current = self.adventurer.position
        print(f"\n>> {current.info} <<")
        
        if not current.was_visited:
            if current.key_here:
                print("На земле лежит ключ!")
            if current.object_here:
                print(f"Здесь находится: {current.object_here}")
        current.was_visited = True
        
        print("\nМожно пойти:")
        for path in current.paths:
            destination = current.paths[path]
            lock_indicator = "(закрыто)" if destination.locked else ""
            print(f"  {path} {lock_indicator}")
    
    def go(self, direction):
        current = self.adventurer.position
        
        if direction in current.paths:
            destination = current.paths[direction]
            
            if destination.locked:
                if self.adventurer.key_count > 0:
                    print("Ключ подошел к замку! Дверь открыта.")
                    destination.locked = False
                    self.adventurer.key_count -= 1
                else:
                    print("Дверь заперта. Требуется ключ.")
                    return
            
            self.adventurer.position = destination
            print(f"Вы двинулись {direction}...")
            
            # Автоматический сбор предметов
            if destination.key_here:
                print("Вы взяли ключ!")
                self.adventurer.key_count += 1
                destination.key_here = False
            
            if destination.object_here:
                print(f"Вы взяли: {destination.object_here}")
                self.adventurer.bag.append(destination.object_here)
                destination.object_here = None
        else:
            print("Нет пути в этом направлении!")
    
    def check_bag(self):
        print("\n=== ВАШИ ВЕЩИ ===")
        print(f"Ключи: {self.adventurer.key_count}")
        if self.adventurer.bag:
print("Предметы в рюкзаке:")
            for num, item in enumerate(self.adventurer.bag, 1):
                print(f"  {num}. {item}")
        else:
            print("Рюкзак пуст")
    
    def apply_item(self):
        if not self.adventurer.bag:
            print("В рюкзаке ничего нет!")
            return
        
        self.check_bag()
        try:
            choice = int(input("\nВыберите предмет для применения: ")) - 1
            if 0 <= choice < len(self.adventurer.bag):
                selected = self.adventurer.bag[choice]
                print(f"Применяем: {selected}")
                
                # Эффекты предметов
                if "аптечка" in selected.lower():
                    print("Здоровье восстановлено!")
                    self.adventurer.bag.pop(choice)
                elif "свиток" in selected.lower():
                    print("Свиток светится магическим светом!")
                else:
                    print("Предмет использован.")
            else:
                print("Неправильный номер!")
        except ValueError:
            print("Введите число!")
    
    def show_commands(self):
        print("\n=== КОМАНДЫ ===")
        print("вперед, назад, лево, право - движение")
        print("рюкзак - посмотреть вещи")
        print("применить - использовать предмет")
        print("команды - эта подсказка")
        print("стоп - закончить игру")
        print("\nНайдите все ключи и выход!")
    
    def start(self):
        print("🌑 ПРИКЛЮЧЕНИЕ В ПОДЗЕМЕЛЬЕ 🌑")
        print("Ищите ключи, открывайте двери и находите выход!")
        self.show_commands()
        
        while True:
            self.show_location()
            
            action = input("\nВаше действие: ").lower().strip()
            
            if action in ["вперед", "назад", "лево", "право"]:
                self.go(action)
            elif action in ["рюкзак", "р"]:
                self.check_bag()
            elif action in ["применить", "п"]:
                self.apply_item()
            elif action in ["команды", "help"]:
                self.show_commands()
            elif action in ["стоп", "exit", "quit"]:
                print("Игра завершена!")
                break
            else:
                print("Неизвестная команда. Напишите 'команды' для помощи.")
            
            # Проверка завершения
            if self.adventurer.position == self.locations["freedom"]:
                print("\n🎇 ВЫ СВОБОДНЫ! ПОДЗЕМЕЛЬЕ ПОБЕЖДЕНО! 🎇")
                print(f"Результат: {self.adventurer.key_count} ключей, {len(self.adventurer.bag)} предметов")
                break

# Запуск
if name == "__main__":
    adventure = DungeonAdventure()
    adventure.start()
