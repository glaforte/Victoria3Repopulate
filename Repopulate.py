from liquid import Template
import json

# Input file paths
NATIONS_FILE = "repopulate/nations.txt"
TEMPLATE_DATA = [
  { 
    "input_file" : "repopulate/building_template.txt",
    "output_file" : "common/history/buildings/00_world_buildings.txt" 
  } , {
    "input_file" : "repopulate/population_template.txt",
    "output_file" : "common/history/population/00_population.txt"
  } , {
    "input_file" : "repopulate/pops_template.txt",
    "output_file" : "common/history/pops/00_all_pops.txt"
  }, {
    "input_file" : "repopulate/countries_template.txt",
    "output_file" : "common/country_definitions/00_countries.txt"
  }
]

def main():
  # Read in the nations file
  with open(NATIONS_FILE, 'r') as f:
    nations = json.load(f)

  # Process the templates individually
  for template_data in TEMPLATE_DATA:
    with open(template_data["input_file"], 'r') as f:
      template_text = f.read()

    # Render
    liquid_template = Template(template_text)
    rendered = liquid_template.render(nations=nations)
    with open(template_data["output_file"], 'w', encoding='utf-8-sig') as f:
      f.write(rendered)

if __name__ == "__main__":
    main()

