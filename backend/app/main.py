from fastapi import FastAPI
from app.models.slide_content import Presentation, Slide, TextBlock, ChartBlock

app = FastAPI(title="Better Presenton API")

@app.get("/")
def read_root():
    return {"status": "Better Presenton Backend is running"}

@app.get("/api/test-schema")
def test_schema_generation():
    """
    Returns a mock presentation to prove our Data Model works.
    This is exactly what the Frontend will receive.
    """
    mock_slide = Slide(
        slide_id="slide_1",
        title="Q3 Financial Overview",
        layout_id="layout_right_chart",
        speaker_notes="Emphasize the 20% growth in the tech sector.",
        blocks=[
            TextBlock(
                block_id="b1",
                content="## Key Highlights\n- Revenue up by **20%**\n- New market entry successful"
            ),
            ChartBlock(
                block_id="b2",
                title="Revenue vs Expenses",
                chart_type="bar",
                x_axis_key="quarter",
                data_keys=["revenue", "expenses"],
                data=[
                    {"quarter": "Q1", "revenue": 4000, "expenses": 2400},
                    {"quarter": "Q2", "revenue": 4500, "expenses": 2600},
                    {"quarter": "Q3", "revenue": 5500, "expenses": 3000},
                ]
            )
        ]
    )
    
    return Presentation(
        presentation_id="pres_123",
        topic="Q3 Review",
        slides=[mock_slide]
    )