from liquid import Template
import json

# Input file paths
NATIONS_FILE = "repopulate/nations.txt"
TEMPLATE_DATA = [
  { 
    "input_file" : "repopulate/building_template.txt",
    "output_file" : "common/history/buildings/rep_initial_buildings.txt" 
  } , {
    "input_file" : "repopulate/population_template.txt",
    "output_file" : "common/history/population/rep_initial_population.txt"
  } , {
    "input_file" : "repopulate/pops_template.txt",
    "output_file" : "common/history/pops/rep_initial_pops.txt"
  }, {
    "input_file" : "repopulate/country_definitions_template.txt",
    "output_file" : "common/country_definitions/rep_countries.txt"
  }, {
    "input_file" : "repopulate/country_laws_template.txt",
    "output_file" : "common/history/countries/rep_country_laws.txt"
  }, {
    "input_file" : "repopulate/strategies_template.txt",
    "output_file" : "common/history/ai/rep_strategies.txt"
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

