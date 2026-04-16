from liquid import Template, Environment
import json
import random
import argparse

# Input file paths

DATA = [
  { "variable" : "nations", "file" : "repopulate/nations.txt"  },
  { "variable" : "strategies", "file" : "repopulate/strategies.txt"  }
]

TEMPLATES = [
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
  }, {
    "input_file" : "repopulate/military_template.txt",
    "output_file" : "common/history/military_formations/rep_armies.txt"
  }, {
    "input_file" : "repopulate/country_name_template.txt",
    "output_file" : "localization/custom_countries_l_english.yml"
  }
]

def random_item(arr):
  return random.choice(arr)

def parse_command_line():
  parser = argparse.ArgumentParser(description="Victoria 3 mod generator")
  parser.add_argument(
      "--seed",
      type=int,
      default=None,
      help="Optional random seed for deterministic output"
  )

  args = parser.parse_args()

  # Apply the seed if provided
  if args.seed is not None:
    seed = args.seed
  else:
    seed = random.randint(1, 10000)

  print(f"Using random seed: {seed}")
  random.seed(seed)

def main():
  # Parse the command-line
  parse_command_line()

  # Read in all the data from files
  liquid_data = {}
  for datum in DATA:
    with open(datum["file"], 'r', encoding='utf-8-sig') as f:
      liquid_data[datum["variable"]] = json.load(f)

  # Process the templates individually
  for template_data in TEMPLATES:
    with open(template_data["input_file"], 'r', encoding='utf-8-sig') as f:
      template_text = f.read()

    # Render

    env = Environment()
    env.add_filter("random_item", random_item)

    liquid_template = env.from_string(template_text)
    rendered = liquid_template.render(liquid_data)
    with open(template_data["output_file"], 'w', encoding='utf-8-sig') as f:
      f.write(rendered)

if __name__ == "__main__":
    main()

