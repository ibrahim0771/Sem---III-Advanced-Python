def title_case(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result["title"] = result["title"].title()
        return result
    return wrapper


def uppercase_body(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result["body"] = [line.upper() for line in result["body"]]
        return result
    return wrapper


class Report:
    separator = "=" * 50

    def __init__(self, title, body):
        self.title = title
        self.body = body

    @classmethod
    def from_template(cls, template, values):
        title = template["title"]
        for key in values:
            title = title.replace("{" + key + "}", str(values[key]))

        body = []
        for line in template["body"]:
            text = line
            for key in values:
                text = text.replace("{" + key + "}", str(values[key]))
            body.append(text)

        return cls(title, body)

    @title_case
    @uppercase_body
    def formatted(self):
        return {
            "title": self.title,
            "body": self.body
        }

    def __str__(self):
        data = self.formatted()
        output = self.separator + "\n"
        output += data["title"] + "\n"
        output += self.separator + "\n"
        output += "\n".join(data["body"])
        return output

    def __len__(self):
        return len(self.body)

    def __add__(self, other):
        return Report(
            self.title + " & " + other.title,
            self.body + other.body
        )


template = {
    "title": "{department} Monthly Report",
    "body": [
        "Manager: {manager}",
        "Revenue: {revenue}",
        "Growth: {growth}"
    ]
}

report1 = Report.from_template(template, {
    "department": "Sales",
    "manager": "Alice",
    "revenue": "$120000",
    "growth": "12%"
})

report2 = Report.from_template(template, {
    "department": "Marketing",
    "manager": "Bob",
    "revenue": "$95000",
    "growth": "8%"
})

combined = report1 + report2

print(report1)
print()
print(combined)
print()
print("Total Sections:", len(combined))
