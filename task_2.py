import json

def vulnerability_report(input_path: str, output_path: str) -> json:
    # Чтение исходного файла
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Обработка json
    vulnerabilities = {}
    for site in data["site"]:
        for alert in site["alerts"]:
            alert_name = alert["alert"]
            alert_count = int(alert["count"])
            if alert_name in vulnerabilities:
                vulnerabilities[alert_name] += alert_count
            else:
                vulnerabilities[alert_name] = alert_count

    # Формирование json-result
    result_json = {
        "vulnerabilities":
            [
                {
                    "name": name,
                    "count": count
                }
                for name, count in vulnerabilities.items()]
    }

    # Запись результата
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(result_json, file, ensure_ascii=False, indent=4)

def main():
    vulnerability_report('input.json', 'result.json')

if __name__ == '__main__':
    main()

