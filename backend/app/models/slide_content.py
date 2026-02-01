from enum import Enum
from typing import List, Optional, Union, Dict, Any
from pydantic import BaseModel, Field, Literal

# --- 1. Enums for Fixed Choices ---
class ChartType(str, Enum):
    BAR = "bar"
    LINE = "line"
    AREA = "area"
    PIE = "pie"
    SCATTER = "scatter"

class DiagramType(str, Enum):
    FLOWCHART = "flowchart"
    SEQUENCE = "sequence"
    MINDMAP = "mindmap"
    GANTT = "gantt"

# --- 2. The Content Blocks (The "Lego Bricks" of a slide) ---

class BaseBlock(BaseModel):
    """Base class for all content blocks"""
    block_id: str = Field(..., description="Unique ID for UI handling")
    
class TextBlock(BaseBlock):
    """Standard text content (Markdown/HTML)"""
    type: Literal["text"] = "text"
    content: str = Field(..., description="Markdown or HTML content")
    style: Optional[str] = Field(None, description="CSS class or style hint")

class ChartBlock(BaseBlock):
    """Editable Chart Data for Recharts"""
    type: Literal["chart"] = "chart"
    title: str
    chart_type: ChartType
    data: List[Dict[str, Any]] = Field(
        ..., 
        description="Array of objects, e.g., [{'name': 'Q1', 'value': 100}]"
    )
    x_axis_key: str = Field(..., description="Key to use for X-Axis (e.g., 'name')")
    data_keys: List[str] = Field(..., description="Keys to plot (e.g., ['revenue', 'profit'])")
    colors: Optional[List[str]] = Field(None, description="Hex codes for bars/lines")

class DiagramBlock(BaseBlock):
    """Editable Diagram Data for Mermaid.js"""
    type: Literal["diagram"] = "diagram"
    diagram_type: DiagramType
    code: str = Field(..., description="Raw Mermaid.js syntax string")
    caption: Optional[str] = None

class ImageBlock(BaseBlock):
    """Image with prompt for regeneration"""
    type: Literal["image"] = "image"
    url: str = Field(..., description="Local path or remote URL")
    alt_text: str
    generation_prompt: Optional[str] = Field(None, description="Prompt used to generate this image")

class TableBlock(BaseBlock):
    """Simple editable table"""
    type: Literal["table"] = "table"
    headers: List[str]
    rows: List[List[str]]

# --- 3. The Slide & Presentation Structure ---

# This Union allows the list to contain any mix of blocks
ContentBlock = Union[TextBlock, ChartBlock, DiagramBlock, ImageBlock, TableBlock]

class Slide(BaseModel):
    slide_id: str
    title: str
    layout_id: str = Field(..., description="ID of the frontend layout template (e.g., 'layout_2col')")
    speaker_notes: Optional[str] = None
    # A slide is just a list of blocks!
    blocks: List[ContentBlock]

class Presentation(BaseModel):
    presentation_id: str
    topic: str
    slides: List[Slide]