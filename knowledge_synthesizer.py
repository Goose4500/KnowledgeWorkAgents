# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "fastmcp>=2.0.0",
#     "pydantic-ai>=0.1.0",
#     "pydantic>=2.0.0",
#     "python-dotenv>=1.0.0",
#     "logfire>=0.1.0",
# ]
# ///

from fastmcp import FastMCP
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import logfire
import asyncio
from typing import List, Dict, Optional

# Load environment variables
load_dotenv()

mcp = FastMCP("knowledge-synthesizer")

logfire.configure()
logfire.instrument_pydantic_ai()

class KnowledgeSynthesis(BaseModel):
    """Structured output for cross-domain knowledge synthesis"""
    synthesis_summary: str
    domain_connections: List[str]
    cross_domain_insights: List[str]
    convergence_patterns: List[str]
    interdisciplinary_opportunities: List[str]
    knowledge_gaps: List[str]
    synthesis_methodology: str
    confidence_scores: Dict[str, float]
    supporting_evidence: List[str]
    citations: List[str]

class InsightMap(BaseModel):
    """Structured output for knowledge relationship mapping"""
    map_summary: str
    relationship_types: List[str]
    connection_strengths: Dict[str, float]
    knowledge_clusters: List[str]
    bridging_concepts: List[str]
    visualization_elements: List[str]
    interaction_patterns: List[str]
    hierarchical_structures: List[str]
    network_properties: Dict[str, float]
    recommended_explorations: List[str]

class StrategicBrief(BaseModel):
    """Structured output for strategic intelligence briefing"""
    executive_summary: str
    key_findings: List[str]
    strategic_implications: List[str]
    stakeholder_impacts: Dict[str, str]
    risk_assessments: List[str]
    opportunity_analysis: List[str]
    competitive_landscape: List[str]
    implementation_roadmap: List[str]
    success_metrics: List[str]
    recommendations: List[str]

class TrendAnalysis(BaseModel):
    """Structured output for trend analysis and prediction"""
    trend_summary: str
    emerging_patterns: List[str]
    trend_trajectories: Dict[str, str]
    disruption_indicators: List[str]
    convergence_signals: List[str]
    weak_signals: List[str]
    scenario_projections: List[str]
    influence_factors: List[str]
    prediction_confidence: Dict[str, float]
    monitoring_recommendations: List[str]

# Connect to MCP servers
semantic_scholar = MCPServerStdio('npx', args=['-y', '@smithery/cli@latest', 'run', '@hamid-vakilzadeh/mcpsemanticscholar', '--key', '4e694cd2-ce2d-4ea7-a742-4990a24854f1'])
fetch = MCPServerStdio('npx', args=['-y', '@smithery/cli@latest', 'run', '@smithery-ai/fetch', '--key', '4e694cd2-ce2d-4ea7-a742-4990a24854f1'])
ultra_crawler = MCPServerStdio('uv', args=['run', '/home/jfloyd/mcp/tools/ultra_simple_crawler_mcp.py'])
notion = MCPServerStdio('npx', args=['-y', '@smithery/cli@latest', 'run', '@smithery-ai/notion', '--key', '4e694cd2-ce2d-4ea7-a742-4990a24854f1'])

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Knowledge synthesis agent
synthesis_agent = Agent(
    "gemini-2.5-flash",
    system_prompt="""You are an expert knowledge synthesizer specializing in cross-domain intelligence and strategic insight generation.

Your expertise covers:
- Cross-domain knowledge synthesis and pattern recognition
- Interdisciplinary connections and convergence analysis
- Strategic intelligence and competitive analysis
- Trend analysis and future scenario planning
- Knowledge mapping and relationship visualization
- Systems thinking and complex adaptive systems
- Innovation patterns and emerging technologies

SYNTHESIS METHODOLOGY:
1. Gather information from multiple domains and sources
2. Identify patterns, connections, and convergence points
3. Synthesize insights that transcend individual domains
4. Generate strategic intelligence for decision-making
5. Create actionable recommendations and roadmaps
6. Visualize knowledge relationships and structures

RESPONSE FORMAT:
Provide comprehensive analysis that demonstrates:
- Deep understanding of multiple domains
- Clear identification of cross-domain connections
- Strategic insights that inform decision-making
- Evidence-based synthesis with proper citations
- Actionable recommendations and next steps
- Confidence assessments for key insights

Focus on generating novel insights that emerge from the intersection of different knowledge domains.""",
    mcp_servers=[semantic_scholar, fetch, ultra_crawler, notion],
    output_type=KnowledgeSynthesis,
    instrument=True
)

# Insight mapping agent
mapping_agent = Agent(
    "gemini-2.5-flash",
    system_prompt="""You are an expert knowledge mapper specializing in visualizing complex relationships and knowledge structures.

Your expertise covers:
- Knowledge graph construction and analysis
- Relationship mapping and network analysis
- Conceptual clustering and taxonomy development
- Information architecture and knowledge organization
- Visualization design and cognitive mapping
- Network theory and graph analytics
- Semantic relationship modeling

MAPPING METHODOLOGY:
1. Analyze topics and identify key concepts
2. Map relationships between concepts and domains
3. Identify connection strengths and types
4. Create hierarchical and network structures
5. Design visualization strategies
6. Recommend exploration pathways

Focus on creating clear, actionable knowledge maps that reveal hidden connections and guide strategic exploration.""",
    mcp_servers=[semantic_scholar, fetch, ultra_crawler, notion],
    output_type=InsightMap,
    instrument=True
)

# Strategic briefing agent
briefing_agent = Agent(
    "gemini-2.5-flash",
    system_prompt="""You are an expert strategic intelligence analyst specializing in executive briefings and decision support.

Your expertise covers:
- Strategic analysis and competitive intelligence
- Stakeholder impact assessment
- Risk and opportunity analysis
- Market and technology assessment
- Policy and regulatory analysis
- Scenario planning and strategic foresight
- Executive communication and briefing

BRIEFING METHODOLOGY:
1. Analyze strategic context and objectives
2. Assess stakeholder interests and impacts
3. Evaluate risks and opportunities
4. Develop actionable recommendations
5. Create implementation roadmaps
6. Define success metrics and KPIs

Focus on providing clear, actionable strategic intelligence that supports executive decision-making.""",
    mcp_servers=[semantic_scholar, fetch, ultra_crawler, notion],
    output_type=StrategicBrief,
    instrument=True
)

# Trend analysis agent
trend_agent = Agent(
    "gemini-2.5-flash",
    system_prompt="""You are an expert trend analyst specializing in emerging pattern recognition and future scenario development.

Your expertise covers:
- Trend analysis and pattern recognition
- Weak signal detection and analysis
- Scenario planning and future studies
- Technology trajectory analysis
- Social and cultural trend mapping
- Disruption theory and innovation cycles
- Predictive modeling and forecasting

ANALYSIS METHODOLOGY:
1. Scan multiple sources for emerging patterns
2. Identify weak signals and early indicators
3. Analyze trend trajectories and convergence
4. Assess disruption potential and impact
5. Develop scenario projections
6. Provide monitoring recommendations

Focus on identifying trends that could significantly impact the specified domain and timeframe.""",
    mcp_servers=[semantic_scholar, fetch, ultra_crawler, notion],
    output_type=TrendAnalysis,
    instrument=True
)

@mcp.tool
async def synthesize_knowledge_domains(domains: List[str], research_question: str, depth: str = "comprehensive") -> str:
    """
    Synthesize knowledge across multiple domains to generate cross-domain insights and novel connections.
    
    This tool conducts comprehensive cross-domain knowledge synthesis by:
    - Analyzing information from multiple specified domains
    - Identifying patterns and connections across domains
    - Generating novel insights that emerge from domain intersections
    - Providing evidence-based synthesis with confidence assessments
    - Creating actionable recommendations for further exploration
    
    Args:
        domains: List of knowledge domains to synthesize (e.g., ["AI", "healthcare", "ethics"])
        research_question: Specific question or challenge to explore across domains
        depth: Analysis depth - "surface", "moderate", or "comprehensive"
    
    Returns:
        Structured knowledge synthesis with cross-domain insights, connections, and recommendations
    """
    
    try:
        synthesis_prompt = f"""
        CROSS-DOMAIN KNOWLEDGE SYNTHESIS REQUEST
        
        Research Question: {research_question}
        Target Domains: {', '.join(domains)}
        Analysis Depth: {depth}
        
        Please conduct comprehensive knowledge synthesis across the specified domains to address the research question. Focus on:
        
        1. DOMAIN ANALYSIS:
        - Gather current knowledge from each domain: {', '.join(domains)}
        - Identify key concepts, theories, and recent developments
        - Search for relevant academic papers and research from 2024-2025
        - Analyze domain-specific methodologies and approaches
        
        2. CROSS-DOMAIN SYNTHESIS:
        - Identify connections and patterns across domains
        - Look for convergence points and shared principles
        - Analyze how insights from one domain inform others
        - Generate novel hypotheses from domain intersections
        
        3. INSIGHT GENERATION:
        - Synthesize findings into actionable insights
        - Identify interdisciplinary opportunities
        - Highlight knowledge gaps and research opportunities
        - Assess confidence levels for key insights
        
        4. EVIDENCE AND VALIDATION:
        - Provide supporting evidence for key insights
        - Include relevant citations and sources
        - Assess the strength of cross-domain connections
        - Identify areas requiring further validation
        
        Use your research capabilities to gather comprehensive information and generate novel insights that emerge from the intersection of these domains.
        """
        
        async with synthesis_agent.run_mcp_servers():
            result = await synthesis_agent.run(synthesis_prompt)
        
        synthesis_data = result.output
        
        # Create structured output
        output = f"""# Cross-Domain Knowledge Synthesis

## Research Question
{research_question}

## Domains Analyzed
{', '.join(domains)}

## Synthesis Summary
{synthesis_data.synthesis_summary}

## Domain Connections
{chr(10).join(f"- {connection}" for connection in synthesis_data.domain_connections)}

## Cross-Domain Insights
{chr(10).join(f"- {insight}" for insight in synthesis_data.cross_domain_insights)}

## Convergence Patterns
{chr(10).join(f"- {pattern}" for pattern in synthesis_data.convergence_patterns)}

## Interdisciplinary Opportunities
{chr(10).join(f"- {opportunity}" for opportunity in synthesis_data.interdisciplinary_opportunities)}

## Knowledge Gaps
{chr(10).join(f"- {gap}" for gap in synthesis_data.knowledge_gaps)}

## Methodology
{synthesis_data.synthesis_methodology}

## Confidence Scores
{chr(10).join(f"- {key}: {value:.2f}" for key, value in synthesis_data.confidence_scores.items())}

## Supporting Evidence
{chr(10).join(f"- {evidence}" for evidence in synthesis_data.supporting_evidence)}

## Citations
{chr(10).join(f"- {citation}" for citation in synthesis_data.citations)}

---
*Generated by Knowledge Synthesizer*
"""
        
        return output
        
    except Exception as e:
        return f"Knowledge synthesis failed: {str(e)}"

@mcp.tool
async def create_insight_maps(topics: List[str], connections: List[str], visualization_type: str = "network") -> str:
    """
    Create comprehensive knowledge relationship maps showing connections between topics and concepts.
    
    This tool generates detailed insight maps by:
    - Analyzing relationships between specified topics
    - Identifying connection types and strengths
    - Creating hierarchical and network structures
    - Designing visualization strategies
    - Recommending exploration pathways
    
    Args:
        topics: List of topics/concepts to map (e.g., ["machine learning", "ethics", "governance"])
        connections: List of known or suspected connections to explore
        visualization_type: Type of visualization - "network", "hierarchy", "cluster", or "flow"
    
    Returns:
        Comprehensive insight map with relationship analysis and visualization recommendations
    """
    
    try:
        mapping_prompt = f"""
        KNOWLEDGE RELATIONSHIP MAPPING REQUEST
        
        Topics to Map: {', '.join(topics)}
        Known Connections: {', '.join(connections)}
        Visualization Type: {visualization_type}
        
        Please create a comprehensive knowledge relationship map for the specified topics. Focus on:
        
        1. TOPIC ANALYSIS:
        - Analyze each topic: {', '.join(topics)}
        - Identify key concepts and sub-topics
        - Research current developments and trends
        - Map semantic relationships and dependencies
        
        2. CONNECTION MAPPING:
        - Explore the specified connections: {', '.join(connections)}
        - Identify additional relationship types
        - Assess connection strengths and directions
        - Map direct and indirect relationships
        
        3. STRUCTURAL ANALYSIS:
        - Create hierarchical topic organization
        - Identify knowledge clusters and communities
        - Find bridging concepts and central nodes
        - Analyze network properties and patterns
        
        4. VISUALIZATION DESIGN:
        - Design {visualization_type} visualization strategy
        - Recommend visual elements and layouts
        - Suggest interaction patterns and navigation
        - Provide exploration pathways and recommendations
        
        Use your research capabilities to gather comprehensive information about these topics and their relationships.
        """
        
        async with mapping_agent.run_mcp_servers():
            result = await mapping_agent.run(mapping_prompt)
        
        mapping_data = result.output
        
        # Create structured output
        output = f"""# Knowledge Relationship Map

## Topics Analyzed
{', '.join(topics)}

## Visualization Type
{visualization_type}

## Map Summary
{mapping_data.map_summary}

## Relationship Types
{chr(10).join(f"- {relationship}" for relationship in mapping_data.relationship_types)}

## Connection Strengths
{chr(10).join(f"- {key}: {value:.2f}" for key, value in mapping_data.connection_strengths.items())}

## Knowledge Clusters
{chr(10).join(f"- {cluster}" for cluster in mapping_data.knowledge_clusters)}

## Bridging Concepts
{chr(10).join(f"- {concept}" for concept in mapping_data.bridging_concepts)}

## Visualization Elements
{chr(10).join(f"- {element}" for element in mapping_data.visualization_elements)}

## Interaction Patterns
{chr(10).join(f"- {pattern}" for pattern in mapping_data.interaction_patterns)}

## Hierarchical Structures
{chr(10).join(f"- {structure}" for structure in mapping_data.hierarchical_structures)}

## Network Properties
{chr(10).join(f"- {key}: {value:.2f}" for key, value in mapping_data.network_properties.items())}

## Recommended Explorations
{chr(10).join(f"- {exploration}" for exploration in mapping_data.recommended_explorations)}

---
*Generated by Knowledge Synthesizer*
"""
        
        return output
        
    except Exception as e:
        return f"Insight mapping failed: {str(e)}"

@mcp.tool
async def generate_strategic_brief(topic: str, stakeholders: List[str], objectives: List[str]) -> str:
    """
    Generate comprehensive strategic intelligence briefings for executive decision-making.
    
    This tool creates strategic briefs by:
    - Analyzing strategic context and competitive landscape
    - Assessing stakeholder interests and impacts
    - Evaluating risks and opportunities
    - Developing actionable recommendations
    - Creating implementation roadmaps with success metrics
    
    Args:
        topic: Strategic topic or challenge to analyze
        stakeholders: List of key stakeholders to consider
        objectives: List of strategic objectives to address
    
    Returns:
        Executive-level strategic brief with analysis, recommendations, and implementation guidance
    """
    
    try:
        briefing_prompt = f"""
        STRATEGIC INTELLIGENCE BRIEFING REQUEST
        
        Strategic Topic: {topic}
        Key Stakeholders: {', '.join(stakeholders)}
        Strategic Objectives: {', '.join(objectives)}
        
        Please generate a comprehensive strategic intelligence briefing on the specified topic. Focus on:
        
        1. STRATEGIC CONTEXT ANALYSIS:
        - Analyze the current state of {topic}
        - Research recent developments and trends
        - Assess competitive landscape and market forces
        - Identify regulatory and policy considerations
        
        2. STAKEHOLDER IMPACT ASSESSMENT:
        - Analyze each stakeholder: {', '.join(stakeholders)}
        - Assess their interests, influence, and potential impacts
        - Identify alignment and conflict areas
        - Evaluate stakeholder response scenarios
        
        3. OBJECTIVE ALIGNMENT:
        - Address each objective: {', '.join(objectives)}
        - Assess feasibility and resource requirements
        - Identify potential conflicts and synergies
        - Prioritize objectives based on strategic value
        
        4. STRATEGIC ANALYSIS:
        - Conduct risk assessment and mitigation strategies
        - Identify opportunities and competitive advantages
        - Analyze implementation challenges and success factors
        - Develop scenario-based strategic options
        
        5. RECOMMENDATIONS AND ROADMAP:
        - Provide clear, actionable recommendations
        - Create implementation timeline and milestones
        - Define success metrics and KPIs
        - Suggest monitoring and evaluation mechanisms
        
        Use your research capabilities to gather comprehensive strategic intelligence and provide executive-level insights.
        """
        
        async with briefing_agent.run_mcp_servers():
            result = await briefing_agent.run(briefing_prompt)
        
        briefing_data = result.output
        
        # Create structured output
        output = f"""# Strategic Intelligence Brief

## Topic
{topic}

## Key Stakeholders
{', '.join(stakeholders)}

## Strategic Objectives
{', '.join(objectives)}

## Executive Summary
{briefing_data.executive_summary}

## Key Findings
{chr(10).join(f"- {finding}" for finding in briefing_data.key_findings)}

## Strategic Implications
{chr(10).join(f"- {implication}" for implication in briefing_data.strategic_implications)}

## Stakeholder Impacts
{chr(10).join(f"- **{stakeholder}**: {impact}" for stakeholder, impact in briefing_data.stakeholder_impacts.items())}

## Risk Assessment
{chr(10).join(f"- {risk}" for risk in briefing_data.risk_assessments)}

## Opportunity Analysis
{chr(10).join(f"- {opportunity}" for opportunity in briefing_data.opportunity_analysis)}

## Competitive Landscape
{chr(10).join(f"- {insight}" for insight in briefing_data.competitive_landscape)}

## Implementation Roadmap
{chr(10).join(f"- {step}" for step in briefing_data.implementation_roadmap)}

## Success Metrics
{chr(10).join(f"- {metric}" for metric in briefing_data.success_metrics)}

## Recommendations
{chr(10).join(f"- {recommendation}" for recommendation in briefing_data.recommendations)}

---
*Generated by Knowledge Synthesizer*
"""
        
        return output
        
    except Exception as e:
        return f"Strategic briefing failed: {str(e)}"

@mcp.tool
async def track_emerging_trends(domain: str, timeframe: str, sources: List[str]) -> str:
    """
    Analyze emerging trends and predict future developments in specified domains.
    
    This tool conducts trend analysis by:
    - Scanning multiple sources for emerging patterns
    - Identifying weak signals and early indicators
    - Analyzing trend trajectories and convergence points
    - Assessing disruption potential and impact
    - Developing scenario projections and monitoring recommendations
    
    Args:
        domain: Domain to analyze for emerging trends (e.g., "artificial intelligence", "healthcare")
        timeframe: Analysis timeframe ("short-term", "medium-term", "long-term")
        sources: List of source types to analyze (e.g., ["academic", "industry", "patents", "startups"])
    
    Returns:
        Comprehensive trend analysis with predictions, scenarios, and monitoring recommendations
    """
    
    try:
        trend_prompt = f"""
        EMERGING TREND ANALYSIS REQUEST
        
        Domain: {domain}
        Timeframe: {timeframe}
        Source Types: {', '.join(sources)}
        
        Please conduct comprehensive trend analysis for the specified domain and timeframe. Focus on:
        
        1. TREND SCANNING:
        - Analyze emerging patterns in {domain}
        - Scan {', '.join(sources)} sources for early indicators
        - Identify breakthrough developments and innovations
        - Research recent publications and developments (2024-2025)
        
        2. PATTERN ANALYSIS:
        - Identify recurring themes and patterns
        - Analyze trend trajectories and momentum
        - Look for convergence points and intersections
        - Assess disruption potential and impact
        
        3. WEAK SIGNAL DETECTION:
        - Identify early-stage developments
        - Analyze fringe innovations and experiments
        - Monitor emerging technologies and methodologies
        - Track regulatory and policy developments
        
        4. SCENARIO DEVELOPMENT:
        - Develop {timeframe} scenario projections
        - Assess probability and impact of different scenarios
        - Identify key influence factors and dependencies
        - Model potential disruption scenarios
        
        5. PREDICTION AND MONITORING:
        - Provide trend predictions with confidence levels
        - Recommend monitoring strategies and indicators
        - Suggest early warning systems and triggers
        - Identify key metrics for trend validation
        
        Use your research capabilities to gather comprehensive trend intelligence from multiple sources.
        """
        
        async with trend_agent.run_mcp_servers():
            result = await trend_agent.run(trend_prompt)
        
        trend_data = result.output
        
        # Create structured output
        output = f"""# Emerging Trend Analysis

## Domain
{domain}

## Timeframe
{timeframe}

## Sources Analyzed
{', '.join(sources)}

## Trend Summary
{trend_data.trend_summary}

## Emerging Patterns
{chr(10).join(f"- {pattern}" for pattern in trend_data.emerging_patterns)}

## Trend Trajectories
{chr(10).join(f"- **{trend}**: {trajectory}" for trend, trajectory in trend_data.trend_trajectories.items())}

## Disruption Indicators
{chr(10).join(f"- {indicator}" for indicator in trend_data.disruption_indicators)}

## Convergence Signals
{chr(10).join(f"- {signal}" for signal in trend_data.convergence_signals)}

## Weak Signals
{chr(10).join(f"- {signal}" for signal in trend_data.weak_signals)}

## Scenario Projections
{chr(10).join(f"- {scenario}" for scenario in trend_data.scenario_projections)}

## Influence Factors
{chr(10).join(f"- {factor}" for factor in trend_data.influence_factors)}

## Prediction Confidence
{chr(10).join(f"- {prediction}: {confidence:.2f}" for prediction, confidence in trend_data.prediction_confidence.items())}

## Monitoring Recommendations
{chr(10).join(f"- {recommendation}" for recommendation in trend_data.monitoring_recommendations)}

---
*Generated by Knowledge Synthesizer*
"""
        
        return output
        
    except Exception as e:
        return f"Trend analysis failed: {str(e)}"

@mcp.resource("synthesis://patterns")
def get_synthesis_patterns() -> str:
    """
    Provides reference patterns for knowledge synthesis and cross-domain analysis.
    """
    
    return """
    KNOWLEDGE SYNTHESIS PATTERNS
    ===========================
    
    1. CONVERGENCE ANALYSIS
    - Identify shared principles across domains
    - Look for parallel developments and solutions
    - Analyze cross-pollination opportunities
    - Map conceptual bridges and translations
    
    2. SYSTEMS THINKING
    - Analyze interconnections and dependencies
    - Identify feedback loops and dynamics
    - Map emergent properties and behaviors
    - Understand multi-level interactions
    
    3. PATTERN RECOGNITION
    - Identify recurring themes and structures
    - Analyze analogies and metaphors
    - Look for universal principles and laws
    - Recognize scaling patterns and invariants
    
    4. CONTRADICTION ANALYSIS
    - Identify tensions and paradoxes
    - Analyze competing perspectives
    - Look for synthesis opportunities
    - Explore creative resolutions
    
    5. EMERGENCE DETECTION
    - Identify weak signals and early indicators
    - Analyze trend intersections and amplifications
    - Look for tipping points and phase transitions
    - Predict emergent phenomena and properties
    
    6. STRATEGIC SYNTHESIS
    - Integrate insights for decision-making
    - Develop actionable recommendations
    - Create implementation strategies
    - Design monitoring and evaluation systems
    """

@mcp.resource("mapping://visualization")
def get_visualization_strategies() -> str:
    """
    Provides guidance for knowledge visualization and mapping strategies.
    """
    
    return """
    KNOWLEDGE VISUALIZATION STRATEGIES
    =================================
    
    1. NETWORK MAPS
    - Node-link diagrams for relationship mapping
    - Force-directed layouts for natural clustering
    - Hierarchical networks for multi-level analysis
    - Dynamic networks for temporal patterns
    
    2. CONCEPT MAPS
    - Hierarchical concept organization
    - Labeled relationship links
    - Cross-links for integration
    - Proposition-based structures
    
    3. KNOWLEDGE GRAPHS
    - Entity-relationship modeling
    - Semantic property representation
    - Ontological structures
    - Linked data integration
    
    4. CLUSTER ANALYSIS
    - Similarity-based grouping
    - Hierarchical clustering
    - Community detection
    - Topical modeling
    
    5. FLOW DIAGRAMS
    - Process and workflow mapping
    - Information flow visualization
    - Causal chain analysis
    - Decision tree structures
    
    6. INTERACTIVE EXPLORATION
    - Drill-down and zoom capabilities
    - Filtering and search functions
    - Multiple view coordination
    - Guided exploration paths
    """

mcp.run()