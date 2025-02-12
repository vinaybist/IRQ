class SecurityPrompts:
    @staticmethod
    def system_prompt():
        return """You are a Security Implementation Expert who specializes in:
1. Converting high-level security controls into detailed technical requirements
2. Providing practical, actionable implementation steps
3. Ensuring compliance with industry standards
4. Recommending best practices for security implementations"""

    @staticmethod
    def implementation_prompt(security_control):
        return f"""Please analyze the following security control and provide comprehensive implementation requirements:

SECURITY CONTROL:
{security_control}

Please structure your response in the following format:

1. TECHNICAL REQUIREMENTS
- Specific hardware/software requirements
- Configuration settings
- Architecture considerations
- Technical parameters

2. IMPLEMENTATION STEPS
- Step-by-step deployment guide
- Configuration procedures
- Testing procedures
- Integration requirements

3. OPERATIONAL REQUIREMENTS
- Monitoring setup
- Maintenance procedures
- Incident response procedures
- Backup and recovery processes

4. COMPLIANCE & DOCUMENTATION
- Relevant standards (e.g., ISO 27001, NIST, etc.)
- Required documentation
- Audit requirements
- Compliance validation steps

For each section, provide specific, actionable details that can be directly implemented by a technical team."""

    @staticmethod
    def validation_prompt(security_control):
        return f"""For the following security control, provide a comprehensive validation framework:

SECURITY CONTROL:
{security_control}

Please provide:
1. Testing criteria
2. Validation methods
3. Success metrics
4. Compliance checkpoints"""


    @staticmethod
    def implementation_prompt2(security_control):
        return f"""For the following security control, provide implementation requirements:

SECURITY CONTROL:
{security_control}

FORMAT YOUR RESPONSE AS FOLLOWS:

1. TECHNICAL REQUIREMENTS
[List technical specifications directly]

2. IMPLEMENTATION STEPS
[List steps directly]

3. OPERATIONAL REQUIREMENTS
[List requirements directly]

4. COMPLIANCE & DOCUMENTATION
[List compliance items directly]

Remember: Start each section directly with the requirements. Do not use any introductory phrases."""
