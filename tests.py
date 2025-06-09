from functions.get_files_info import get_files_info

def run_tests():
    print("Running tests...\n")

    print("Test 1: get_files_info('calculator', '.')")
    print(get_files_info("calculator", "."))
    print("\n---\n")

    print("Test 2: get_files_info('calculator', 'pkg')")
    print(get_files_info("calculator", "pkg"))
    print("\n---\n")

    print("Test 3: get_files_info('calculator', '/bin')")
    print(get_files_info("calculator", "/bin"))
    print("\n---\n")

    print("Test 4: get_files_info('calculator', '../')")
    print(get_files_info("calculator", "../"))
    print("\n---\n")

if __name__ == "__main__":
    run_tests()