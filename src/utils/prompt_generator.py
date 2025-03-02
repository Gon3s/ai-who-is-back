import json
from pathlib import Path
from typing import Dict, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PromptGenerator:
    def __init__(self, base_path: Path):
        """Initialise le générateur de prompts."""
        self.base_path = base_path
        self.template_path = (
            base_path / "data" / "prompts" / "character_prompt_template.txt"
        )
        self.stub_path = base_path / "data" / "stub_data.json"
        self.output_dir = base_path / "data" / "prompts" / "characters"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def load_template(self) -> str:
        """Charge le template de prompt."""
        try:
            with open(self.template_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            logger.error(f"Template file not found at {self.template_path}")
            raise

    def load_stub_data(self) -> List[Dict]:
        """Charge les données du stub JSON."""
        try:
            with open(self.stub_path, "r", encoding="utf-8") as f:
                return json.load(f)["characters"]
        except FileNotFoundError:
            logger.error(f"Stub data file not found at {self.stub_path}")
            raise

    def format_attribute(self, attr: str, value: any) -> str:
        """Formate les attributs en descriptions naturelles."""
        if isinstance(value, bool):
            if attr == "has_glasses":
                return "wearing modern glasses" if value else "no glasses"
            elif attr == "has_beard":
                return "with a well-groomed beard" if value else "clean-shaven"
            elif attr == "has_hat":
                return "wearing a casual hat" if value else "no hat"
        return str(value)

    def generate_prompt(self, character: Dict) -> str:
        """Génère le prompt pour un personnage."""
        template = self.load_template()

        # Prépare tous les attributs pour le remplacement
        replacements = {
            "name": character["name"],
            "hair_color": character["hair_style"]
            if character["hair_style"] != "bald"
            else "",
            "hair_style": character["hair_style"],
            "eye_color": character["eye_color"],
            "has_glasses": self.format_attribute(
                "has_glasses", character["has_glasses"]
            ),
            "has_beard": self.format_attribute("has_beard", character["has_beard"]),
            "has_hat": self.format_attribute("has_hat", character["has_hat"]),
            "gender": character["gender"],
            "height": character["height"],
            "age_range": character["age_range"],
            "style": character["style"],
            "skin_tone": character["skin_tone"],
        }

        # Remplace tous les placeholders dans le template
        prompt = template
        for key, value in replacements.items():
            prompt = prompt.replace(f"[{key}]", value)

        return prompt

    def save_prompt(self, character_name: str, prompt: str):
        """Sauvegarde le prompt dans un fichier."""
        output_path = self.output_dir / f"{character_name.lower()}.txt"
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(prompt)
            logger.info(f"Generated prompt for {character_name}")
        except IOError as e:
            logger.error(f"Error saving prompt for {character_name}: {e}")

    def generate_all_prompts(self):
        """Génère les prompts pour tous les personnages."""
        characters = self.load_stub_data()

        for character in characters:
            prompt = self.generate_prompt(character)
            self.save_prompt(character["name"], prompt)

        logger.info(f"Generated {len(characters)} character prompts")


def main():
    base_path = Path(__file__).parent.parent.parent
    generator = PromptGenerator(base_path)
    generator.generate_all_prompts()


if __name__ == "__main__":
    main()
