from app.entities.menu import Section


class MenuServices:
    @staticmethod
    def sort_menu(sections: list[Section], subsections: list[Section]):
        sections_with_subsections = {section.name: [] for section in sections}
        for subsection in subsections:
            sections_with_subsections[subsection.parent].append(subsection)
        ordered_menu = []
        for section in sections:
            ordered_menu.append(section)
            ordered_menu.extend(sections_with_subsections[section.name])
        return ordered_menu
