from useful.print_color import PrintColor

if __name__ == '__main__':
    PrintColor.good("12233", "ssss", [1, 2, 3, 4], {"name": "abc", "value": 334})
    PrintColor.red("12233", "ssss", [1, 2, 3, 4], {"name": "abc", "value": 334},sep=",")
    PrintColor.blue("12233", "ssss", [1, 2, 3, 4], {"name": "abc", "value": 334},sep=" ")

    PrintColor.white("sss", "xxx")
