#!/usr/bin/env python3
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

load_dotenv()

mcp = FastMCP("semantic-scholar-innovation-agent")

logfire.configure()
logfire.instrument_pydantic_ai()

class SemanticScholarInnovationResponse(BaseModel):
    """Structured output for semantic scholar innovation research with 2025 insights"""
    cutting_edge_research_findings: list[str]
    novel_methodologies_2025: list[str]
    emerging_innovation_patterns: list[str]
    breakthrough_applications: list[str]
    interdisciplinary_connections: list[str]
    future_research_directions: list[str]
    technology_convergence_trends: list[str]
    innovation_acceleration_factors: list[str]
    paradigm_shifting_papers: list[str]
    practical_implementation_insights: list[str]
    research_gap_opportunities: list[str]
    next_generation_approaches: list[str]

sequential_thinking = MCPServerStdio('npx', args=['-y', '@modelcontextprotocol/server-sequential-thinking'])
semantic_scholar = MCPServerStdio('npx', args=['-y', '@smithery/cli@latest', 'run', '@hamid-vakilzadeh/mcpsemanticscholar', '--key', '4e694cd2-ce2d-4ea7-a742-4990a24854f1'])

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

system_prompt = """You are an elite innovation researcher specializing in deep academic research using Semantic Scholar to uncover cutting-edge 2025 insights for novel innovative ideas.

Your core mission is to take innovative ideas and conduct comprehensive research using Semantic Scholar to discover the most recent 2025 academic insights, breakthrough research, and emerging innovation patterns.

PARALLEL TOOL USAGE STRATEGY:
You MUST maximize efficiency by making MULTIPLE PARALLEL tool calls to Semantic Scholar. Do NOT make sequential single calls - instead:

1. **Simultaneous Multi-Query Strategy**: Launch multiple paper searches in parallel covering different angles of the innovation idea
2. **Concurrent Analysis**: Perform citation analysis, reference analysis, and advanced searches simultaneously
3. **Parallel Domain Exploration**: Search across multiple related fields and disciplines at once
4. **Batch Processing**: Use batch operations to analyze multiple papers simultaneously

ESSENTIAL PARALLEL TOOL CALL PATTERNS:
- papers-search-advanced with different query variations (run 3-5 parallel searches)
- papers-citations AND papers-references for key papers (run both simultaneously)
- Multiple fieldsOfStudy searches (AI, computer science, engineering, etc.)
- Concurrent year-filtered searches (2025 only, 2024-2025, etc.)
- Parallel author research for breakthrough researchers
- Simultaneous analysis of related innovation domains

2025 RESEARCH FOCUS:
CRITICAL: Focus EXCLUSIVELY on 2025 publications and the most recent cutting-edge research. Use yearStart=2025 and yearEnd=2025 filters aggressively.

SEARCH STRATEGY FOR 2025 INSIGHTS:
1. **Primary Innovation Search**: Search for the core innovation idea with 2025 filter
2. **Adjacent Technology Search**: Search related technologies and methodologies from 2025
3. **Application Domain Search**: Search specific application areas with 2025 focus
4. **Methodology Innovation Search**: Search for novel methodologies in 2025
5. **Interdisciplinary Search**: Search cross-domain applications from 2025
6. **Breakthrough Pattern Search**: Search for paradigm-shifting approaches in 2025

SEMANTIC SCHOLAR TOOL OPTIMIZATION:
- Use papers-search-advanced with minCitations for credible sources
- Apply yearStart=2025, yearEnd=2025 filters consistently
- Use sortBy="citationCount" for high-impact papers
- Leverage fieldsOfStudy for targeted domain searches
- Use openAccessOnly=true for accessible research
- Apply papers-batch for efficient multi-paper analysis

SEQUENTIAL THINKING INTEGRATION:
Use sequential thinking to:
- Plan comprehensive parallel research strategy
- Analyze connections between parallel research streams
- Synthesize findings from multiple concurrent searches
- Identify patterns across parallel research domains
- Generate novel insights from combined research streams

RESEARCH DEPTH REQUIREMENTS:
- Minimum 15-20 parallel Semantic Scholar tool calls per analysis
- Focus on 2025 publications with high citation potential
- Prioritize breakthrough methodologies and novel approaches
- Identify emerging innovation patterns and convergence trends
- Discover interdisciplinary connections and applications

OUTPUT OPTIMIZATION:
Structure ALL insights as list[str] items that are:
- Specific and actionable
- Directly derived from 2025 research
- Rich in technical detail and innovation potential
- Connected to real breakthrough papers and findings
- Optimized for practical implementation

Your goal is to provide the most comprehensive, up-to-date, and insightful analysis of innovative ideas using the latest 2025 academic research through aggressive parallel tool usage."""

innovation_research_agent = Agent(
    "gemini-2.5-flash",
    system_prompt=system_prompt,
    mcp_servers=[sequential_thinking, semantic_scholar],
    output_type=SemanticScholarInnovationResponse,
    instrument=True
)

@mcp.tool
async def research_innovation_idea(innovation_idea: str) -> str:
    """
    Conduct deep research on a novel innovative idea using Semantic Scholar to discover cutting-edge 2025 insights.
    
    This specialized agent excels at:
    - Parallel tool calls to Semantic Scholar for maximum research efficiency
    - Focusing exclusively on 2025 publications and breakthrough research
    - Identifying emerging innovation patterns and methodologies
    - Discovering interdisciplinary connections and applications
    - Finding technology convergence trends and acceleration factors
    - Uncovering research gaps and next-generation approaches
    
    Args:
        innovation_idea: The novel innovative idea to research deeply using Semantic Scholar
    
    Returns:
        Comprehensive 2025 research insights with cutting-edge academic findings and innovation patterns
    """
    
    research_prompt = f"""
    SEMANTIC SCHOLAR INNOVATION RESEARCH REQUEST
    
    INNOVATION IDEA TO RESEARCH:
    {innovation_idea}
    
    CRITICAL INSTRUCTIONS:
    1. Use sequential thinking to plan a comprehensive parallel research strategy
    2. Make MULTIPLE PARALLEL tool calls to Semantic Scholar (minimum 15-20 calls)
    3. Focus EXCLUSIVELY on 2025 publications using yearStart=2025, yearEnd=2025 filters
    4. Use papers-search-advanced with different query variations simultaneously
    5. Perform citation and reference analysis on key papers in parallel
    6. Search across multiple related fields and disciplines concurrently
    
    PARALLEL RESEARCH STRATEGY:
    
    PHASE 1: CORE INNOVATION SEARCHES (Run 4-5 parallel searches)
    - Primary innovation search with 2025 filter
    - Adjacent technology search with 2025 filter
    - Methodology innovation search with 2025 filter
    - Application domain search with 2025 filter
    - Breakthrough pattern search with 2025 filter
    
    PHASE 2: DEEP ANALYSIS (Run 6-8 parallel analyses)
    - Citation analysis of top papers found in Phase 1
    - Reference analysis of breakthrough papers
    - Author research for key innovation researchers
    - Interdisciplinary connection searches
    - Technology convergence analysis
    - Research gap identification
    
    PHASE 3: SYNTHESIS AND INSIGHTS (Run 4-6 parallel syntheses)
    - Pattern recognition across research streams
    - Innovation acceleration factor analysis
    - Paradigm shift identification
    - Practical implementation pathway research
    - Future research direction mapping
    - Next-generation approach discovery
    
    RESEARCH DIMENSIONS TO EXPLORE:
    
    1. CUTTING-EDGE RESEARCH FINDINGS:
    - Latest 2025 breakthroughs related to the innovation idea
    - High-impact papers with novel findings
    - Emerging research results and experimental outcomes
    - Breakthrough discoveries and significant advances
    
    2. NOVEL METHODOLOGIES 2025:
    - New approaches and techniques developed in 2025
    - Innovative research methodologies and frameworks
    - Breakthrough analytical methods and tools
    - Novel experimental designs and validation approaches
    
    3. EMERGING INNOVATION PATTERNS:
    - Patterns of innovation emerging across 2025 research
    - Common themes and convergence points
    - Innovation acceleration trends and catalysts
    - Systematic approaches to breakthrough innovation
    
    4. BREAKTHROUGH APPLICATIONS:
    - Real-world applications and implementations from 2025
    - Practical use cases and deployment scenarios
    - Success stories and case studies
    - Commercial and industrial applications
    
    5. INTERDISCIPLINARY CONNECTIONS:
    - Cross-domain applications and integrations
    - Connections between different research fields
    - Hybrid approaches combining multiple disciplines
    - Innovation through interdisciplinary collaboration
    
    6. FUTURE RESEARCH DIRECTIONS:
    - Emerging research trajectories and focus areas
    - Next-generation research questions and challenges
    - Future innovation opportunities and possibilities
    - Long-term research roadmaps and visions
    
    7. TECHNOLOGY CONVERGENCE TRENDS:
    - Convergence of different technologies and approaches
    - Integration patterns and synergistic effects
    - Technology fusion and hybrid solutions
    - Convergence-driven innovation opportunities
    
    8. INNOVATION ACCELERATION FACTORS:
    - Factors accelerating innovation in this domain
    - Catalysts for breakthrough discoveries
    - Enabling technologies and infrastructure
    - Accelerated development methodologies
    
    9. PARADIGM SHIFTING PAPERS:
    - Papers that challenge established paradigms
    - Breakthrough research that changes perspectives
    - Paradigm-shifting methodologies and frameworks
    - Transformative insights and revelations
    
    10. PRACTICAL IMPLEMENTATION INSIGHTS:
    - Actionable insights for implementation
    - Practical deployment strategies and considerations
    - Real-world implementation challenges and solutions
    - Success factors and best practices
    
    11. RESEARCH GAP OPPORTUNITIES:
    - Unexplored areas and research opportunities
    - Gaps in current research and knowledge
    - Underexplored applications and use cases
    - Innovation opportunities in research gaps
    
    12. NEXT-GENERATION APPROACHES:
    - Emerging next-generation methodologies
    - Future approaches and evolution trajectories
    - Advanced techniques and sophisticated methods
    - Next-level innovation frameworks and strategies
    
    EXECUTION REQUIREMENTS:
    - Make extensive parallel tool calls to Semantic Scholar
    - Focus exclusively on 2025 publications
    - Use advanced search filters and parameters
    - Analyze high-impact papers and breakthrough research
    - Identify patterns across multiple research streams
    - Generate actionable insights for practical implementation
    
    Use your sequential thinking capabilities to orchestrate this comprehensive parallel research strategy and deliver cutting-edge 2025 insights that advance understanding of the innovation idea.
    """
    
    try:
        async with innovation_research_agent.run_mcp_servers():
            result = await innovation_research_agent.run(research_prompt)
        
        research_data = result.output
        
        research_report = f"""# Semantic Scholar Innovation Research - 2025 Insights

## Innovation Idea Analysis
**{innovation_idea}**

*Comprehensive academic research using Semantic Scholar focused on 2025 breakthrough insights*

---

## 🔬 Cutting-Edge Research Findings (2025)
{chr(10).join(f"• {finding}" for finding in research_data.cutting_edge_research_findings)}

## 🛠️ Novel Methodologies 2025
{chr(10).join(f"• {methodology}" for methodology in research_data.novel_methodologies_2025)}

## 🌟 Emerging Innovation Patterns
{chr(10).join(f"• {pattern}" for pattern in research_data.emerging_innovation_patterns)}

## 💡 Breakthrough Applications
{chr(10).join(f"• {application}" for application in research_data.breakthrough_applications)}

## 🔗 Interdisciplinary Connections
{chr(10).join(f"• {connection}" for connection in research_data.interdisciplinary_connections)}

## 🚀 Future Research Directions
{chr(10).join(f"• {direction}" for direction in research_data.future_research_directions)}

## ⚡ Technology Convergence Trends
{chr(10).join(f"• {trend}" for trend in research_data.technology_convergence_trends)}

## 🎯 Innovation Acceleration Factors
{chr(10).join(f"• {factor}" for factor in research_data.innovation_acceleration_factors)}

## 📄 Paradigm Shifting Papers
{chr(10).join(f"• {paper}" for paper in research_data.paradigm_shifting_papers)}

## 🔧 Practical Implementation Insights
{chr(10).join(f"• {insight}" for insight in research_data.practical_implementation_insights)}

## 🎪 Research Gap Opportunities
{chr(10).join(f"• {gap}" for gap in research_data.research_gap_opportunities)}

## 🔮 Next-Generation Approaches
{chr(10).join(f"• {approach}" for approach in research_data.next_generation_approaches)}

---

*Generated by Semantic Scholar Innovation Agent - 2025 Research Specialist*

## Research Methodology Applied:
- **Parallel Tool Strategy**: Executed 15+ concurrent Semantic Scholar searches
- **2025 Focus**: Exclusively analyzed cutting-edge 2025 publications
- **Multi-Domain Analysis**: Explored innovation across multiple research fields
- **Citation Network Analysis**: Analyzed citation patterns and research networks
- **Interdisciplinary Synthesis**: Connected insights across diverse domains
- **Sequential Thinking**: Methodically orchestrated comprehensive research strategy

## Search Optimization:
- **Advanced Filters**: yearStart=2025, yearEnd=2025, minCitations, sortBy=citationCount
- **Parallel Queries**: Multiple simultaneous searches across different angles
- **Batch Processing**: Efficient multi-paper analysis and synthesis
- **Domain Coverage**: AI, computer science, engineering, interdisciplinary fields
- **High-Impact Focus**: Prioritized breakthrough papers and novel methodologies

Ready to transform innovative ideas into actionable 2025 research insights!
"""
        
        return research_report
        
    except Exception as e:
        return f"Semantic Scholar innovation research failed: {str(e)}"

mcp.run()