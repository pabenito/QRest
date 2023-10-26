from app.core.entities.menu import Section


class IMenuRepository:
    def get_all_sections(self) -> list[Section]:
        pass

    def get_all_subsections(self) -> list[Section]:
        pass
