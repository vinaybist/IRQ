class SecurityPrompts:
    @staticmethod
    def system_prompt():
        return """You are a Security Implementation Expert who specializes in:
1. Converting high-level security controls into detailed technical requirements
2. Providing practical, actionable implementation steps
3. Ensuring compliance with industry standards
4. Recommending best practices for security implementations"""

    @staticmethod
    def system_prompt2():
        return """You are a Security Implementation Expert. Your responses should:
- Be direct and concise without any conversational phrases
- Never start with phrases like "Here is", "Sure", "I'll help", etc.
- Never include introductions or conclusions
- Start directly with the requirements
- Use clear, professional technical language"""
    
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


    @staticmethod
    def system_prompt2():
        return """You are a Security Implementation Expert. For each security requirement:
1. First, analyze the requirement's core objectives
2. Then, consider potential implementation challenges
3. Next, evaluate security implications
4. Finally, provide specific implementation details

Structure your thinking process explicitly before providing final recommendations."""

    @staticmethod
    def implementation_prompt2(security_control):
        return f"""Analyze the following security control using step-by-step reasoning:

SECURITY CONTROL:
{security_control}

Let's think about this systematically:

1. REQUIREMENT ANALYSIS
- What is the core objective?
- What are the key security principles involved?
- Who are the stakeholders?

2. IMPLEMENTATION CONSIDERATIONS
- What technical components are needed?
- What are potential implementation challenges?
- What existing systems need to be considered?

3. SECURITY IMPLICATIONS
- What are the potential security risks?
- What compensating controls are needed?
- How does this affect the overall security posture?

Based on this analysis, provide:

1. TECHNICAL REQUIREMENTS
[Derived from analysis]

2. IMPLEMENTATION STEPS
[Based on considerations]

3. OPERATIONAL REQUIREMENTS
[Addressing identified needs]

4. COMPLIANCE & DOCUMENTATION
[Meeting regulatory requirements]"""
