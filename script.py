#!/usr/bin/env python3
import yaml
import os
import sys
import glob
from pprint import pformat

def load_yaml_file(file_path):
    """Load a YAML file and return its contents."""
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error loading YAML file {file_path}: {e}")
        return None

def find_control_file(control_id, yaml_dir):
    """Find a YAML file with the specified control ID."""
    # Look for files that match the pattern in the directory
    pattern = os.path.join(yaml_dir, f"*{control_id}*.yaml")
    matching_files = glob.glob(pattern)
    
    # Also try .yml extension
    if not matching_files:
        pattern = os.path.join(yaml_dir, f"*{control_id}*.yml")
        matching_files = glob.glob(pattern)
    
    if matching_files:
        return matching_files[0]
    return None

def get_part_content(yaml_data, part_name):
    """Extract content from a specific part in the YAML."""
    if 'parts' in yaml_data and yaml_data['parts']:
        for part in yaml_data['parts']:
            if part.get('name') == part_name:
                return part.get('prose', '')
    return None

def process_req_file(req_file_path, yaml_dir):
    """Process a requirement YAML file and display the integrated view."""
    # Load the requirement YAML
    req_yaml = load_yaml_file(req_file_path)
    if not req_yaml:
        return "Failed to load requirement YAML file"
    
    # Get the control mappings
    control_mappings = req_yaml.get('control_mappings', [])
    if not control_mappings:
        return "No control mappings found in the requirement YAML"
    
    # Get statement, verification, and guidance from the requirement YAML
    statement = get_part_content(req_yaml, 'statement')
    verification = get_part_content(req_yaml, 'verification')
    guidance = get_part_content(req_yaml, 'guidance')
    
    results = []
    results.append(f"Requirement File: {req_file_path}")
    results.append(f"Title: {req_yaml.get('title', 'Unknown')}")
    results.append(f"ID: {req_yaml.get('id', 'Unknown')}")
    results.append(f"Version: {req_yaml.get('version', 'Unknown')}")
    results.append(f"\nControl Mappings: {', '.join(control_mappings)}")
    
    # Process each control mapping
    for control_id in control_mappings:
        results.append(f"\n{'='*50}")
        results.append(f"Control ID: {control_id}")
        
        # Find and load the corresponding control YAML
        control_file = find_control_file(control_id, yaml_dir)
        if control_file:
            control_yaml = load_yaml_file(control_file)
            if control_yaml:
                results.append(f"Control Title: {control_yaml.get('title', 'Unknown')}")
                
                # Extract control objective
                objective = get_part_content(control_yaml, 'objective')
                results.append("\n1. Control Objective:")
                if objective:
                    if isinstance(objective, list):
                        for item in objective:
                            results.append(f"   - {item}")
                    else:
                        results.append(f"   {objective}")
                else:
                    results.append("   Not specified")
                
                # Use the statement from the requirement YAML
                results.append("\n2. Control Statement:")
                if statement:
                    if isinstance(statement, list):
                        for item in statement:
                            results.append(f"   - {item}")
                    else:
                        results.append(f"   {statement}")
                else:
                    results.append("   Not specified")
                
                # Use the verification from the requirement YAML
                results.append("\n3. Verification:")
                if verification:
                    if isinstance(verification, list):
                        for item in verification:
                            results.append(f"   - {item}")
                    else:
                        results.append(f"   {verification}")
                else:
                    results.append("   Not specified")
                
                # Use the guidance from the requirement YAML
                results.append("\n4. Guidance:")
                if guidance:
                    if isinstance(guidance, list):
                        for item in guidance:
                            results.append(f"   - {item}")
                    else:
                        results.append(f"   {guidance}")
                else:
                    results.append("   Not specified")
            else:
                results.append(f"Failed to load control file: {control_file}")
        else:
            results.append(f"No control file found for ID: {control_id}")
    
    return "\n".join(results)

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <req_yaml_file> <yaml_directory>")
        sys.exit(1)
    
    req_file = sys.argv[1]
    yaml_dir = sys.argv[2]
    
    result = process_req_file(req_file, yaml_dir)
    print(result)

if __name__ == "__main__":
    main()
