from manim import *
from manim import Line


class MOSFETOperation(Scene):
    def construct(self):
        source = VGroup(
            Rectangle(width=1, height=2, color=YELLOW, fill_opacity=0.5).move_to(LEFT * 4 + DOWN * 1.0)
        )
        border_source = Rectangle(width=1.1, height=2, color=RED, fill_opacity=0, stroke_width=10).move_to(LEFT * 4 + DOWN * 1.0)

        drain = VGroup(
            Rectangle(width=1, height=2, color=YELLOW, fill_opacity=0.5).move_to(RIGHT * 4 + DOWN * 1.0).move_to(RIGHT * 4 + DOWN * 1.0)
        )
        channel = Rectangle(width=6.9, height=0.5, color=YELLOW, fill_opacity=0.5).move_to(DOWN * 1)

        lower_border = Rectangle(width=channel.get_width(), height=0.1, color=RED, fill_opacity=1).move_to(DOWN * 1.25)
        border_drain = Rectangle(width=1.1, height=2, color=RED, fill_opacity=0, stroke_width=10).move_to(RIGHT * 4 + DOWN * 1.0)

        gate = Rectangle(width=1, height=1.5, color=GREEN, fill_opacity=0.5).move_to(UP * 0)
        VGS = Rectangle(width=1.3, height=0.5, color=WHITE, fill_opacity=0.5).move_to(UP * 3 + RIGHT * 1)
        VDS = Rectangle(width=1, height=0.5, color=WHITE, fill_opacity=0.5).move_to(UP * 2 + LEFT * 3)
        GND = Rectangle(width=1, height=0.5, color=WHITE, fill_opacity=0.5).move_to(DOWN * 3.7 + LEFT * 5)
        SUBSTRATE = Rectangle(width=1, height=0.5, color=WHITE, fill_opacity=0.5).move_to(DOWN * 3)
        width_gate = Rectangle(width=9.3, height=0.5, color=ORANGE, fill_opacity=0.5).move_to(LEFT * 0.0 + DOWN * 2.5)

        electrons = VGroup(*[Dot(radius=0.05, color=BLUE) for _ in range(20)])
        electrons.arrange_in_grid(buff=0.3)
        electrons.move_to(LEFT * 2 + DOWN * 0.7)

        line1 = Line(width_gate.get_bottom(), SUBSTRATE.get_top(), color=PURPLE, stroke_width=5)
        line_GND_vertical = Line(SUBSTRATE.get_bottom(), SUBSTRATE.get_bottom() + DOWN *0.5, color=PURPLE, stroke_width=5)
        line_GND = Line(GND.get_right(), line_GND_vertical.get_end(), color=PURPLE, stroke_width=5)
        horizontal_line1 = Line(VGS.get_left(), VGS.get_left() + LEFT * 4.3, color=PURPLE, stroke_width=5)
        vertical_line1 = Line(horizontal_line1.get_end(), source.get_top(), color=PURPLE, stroke_width=5)
        horizontal_line_drain = Line(VGS.get_right(), VGS.get_right() + RIGHT * 2.4, color=PURPLE, stroke_width=5)
        vertical_line_drain = Line(horizontal_line_drain.get_end(), drain.get_top(), color=PURPLE, stroke_width=5)
        line_VGS_GND1 = Line(GND.get_top(), GND.get_top() + UP * 6.45, color=PURPLE, stroke_width=5)
        line_VGS_GND2 = Line(line_VGS_GND1.get_end(), horizontal_line1.get_end(), color=PURPLE, stroke_width=5)
        line_VDS_source = Line(VDS.get_left(), VDS.get_left() + LEFT * 0.4, color=PURPLE, stroke_width=5)
        line_VDS_gate_horizontal = Line(VDS.get_right(), VDS.get_right() + RIGHT * 2.5, color=PURPLE, stroke_width=5)
        line_VDS_gate_vertical = Line(gate.get_top(), line_VDS_gate_horizontal.get_end(), color=PURPLE, stroke_width=5)
        gate_text = Text("Gate", color=GREEN, font_size=15).move_to(UP * 1, RIGHT * 0.5)
        gate_positive = Text("+", color=RED).move_to(UP * 1 + RIGHT * 0.7)
        VDS_positive = Text("+", color=RED).move_to(UP * 2.2 + LEFT * 2.3)
        VGS_positive = Text("+", color=RED).move_to(UP * 3.2 + RIGHT * 1.9)
        source_text = Text("Source", color=YELLOW, font_size=15).move_to(LEFT * 3 + UP * 0.5)
        GND_text = Text("GND", color=WHITE, font_size=15).move_to(LEFT * 6 + DOWN * 3.3)
        drain_text = Text("Drain", color=RED, font_size=15).move_to(RIGHT * 5 + UP * 0.5)
        channel_text = Text("Channel", color=YELLOW, font_size=15).move_to(RIGHT * 1.5 + DOWN * 0.5)

        substrate_text = Text("Substrate_connection", color=WHITE, font_size=15).move_to(RIGHT * 1 + DOWN * 3.4)
        width_gate_text = Text("substrate", color=ORANGE, font_size=15).move_to(RIGHT * 1.5 + DOWN * 2)

        self.play(FadeIn(source), FadeIn(drain), FadeIn(gate), FadeIn(channel),
                  FadeIn(gate_positive), FadeIn(width_gate),
                  FadeIn(source_text), FadeIn(drain_text), FadeIn(gate_text),
                  FadeIn(channel_text), FadeIn(width_gate_text), FadeIn(border_source), FadeIn(border_drain),
                  FadeIn(VDS), FadeIn(VGS), FadeIn(VDS_positive), FadeIn(VGS_positive),
                  FadeIn(GND), FadeIn(SUBSTRATE), FadeIn(substrate_text), FadeIn(GND_text), FadeIn(line1), FadeIn(horizontal_line1), FadeIn(vertical_line1), FadeIn(horizontal_line_drain),
                  FadeIn(vertical_line_drain), FadeIn(line_GND), FadeIn(line_GND_vertical), FadeIn(line_VGS_GND1), FadeIn(line_VGS_GND2), FadeIn(line_VDS_source), FadeIn(line_VDS_gate_horizontal),
                  FadeIn(line_VDS_gate_vertical),FadeIn(lower_border) )

        # Поява електронів
        self.play(FadeIn(electrons))
        self.wait(1)
        # Рух електронів праворуч
        self.play(ApplyMethod(electrons.shift, RIGHT * 4), run_time=2)
        self.wait(1)
        # Зникнення електронів
        self.play(FadeOut(electrons))
        self.wait(1)

        electrons.move_to(LEFT * 2 + DOWN * 0.7)  # установка електронів на початок каналу

        # Друга поява електронів на початку каналу
        self.play(FadeIn(electrons))
        self.wait(1)
        # Звуження затвору Мосфета у стані насичення
        self.play(ApplyMethod(lower_border.stretch, 3.5, 1, {"about_edge": DOWN}), run_time=3)
        self.play(ApplyMethod(electrons.shift, RIGHT * 4), run_time=5)
        self.wait(1)

        self.play(ApplyMethod(lower_border.stretch, 1/3.5, 1, {"about_edge": DOWN}), run_time=3)
        self.wait(1)

        # Повторне зникнення електронів
        self.play(FadeOut(electrons))
        self.wait(1)
        electrons.move_to(LEFT * 2 + DOWN * 0.7)  # установка електронів на початок каналу

        # Повторна поява електронів
        self.play(FadeIn(electrons))
        self.wait(1)
        # Рух електронів праворуч після збільшення напруги на Vgs для розширення каналу
        self.play(ApplyMethod(electrons.shift, RIGHT * 4), run_time=2)
        self.wait(1)

if __name__ == "__main__":
    # To render the animation, use:
    # python -m manim main.py MOSFETOperation -pql --fps 60
    pass
