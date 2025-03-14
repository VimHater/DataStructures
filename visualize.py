from manim import *

class CreateNode(Scene):
    def construct(self):
        # Parameters for node
        rect_width = 2
        rect_height = 1

        # Title
        title = Text("Tạo một Node", font="Times New Roman").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 1: Create the structure
        step1 = Text("Bước 1:Tạo một struct node", font="Times New Roman").scale(0.7).next_to(title, DOWN)
        self.play(Write(step1))

        # Show the structure diagram
        data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=WHITE)
        pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=WHITE)

        structure = VGroup(data_rect, pointer_rect).arrange(RIGHT, buff=0)
        structure.move_to([0, 1, 0])

        data_label = Text("Data").scale(0.6).move_to(data_rect.get_center())
        pointer_label = Text("Next").scale(0.6).move_to(pointer_rect.get_center())

        self.play(Create(structure))
        self.play(Write(data_label), Write(pointer_label))
        self.wait(1)

        # Step 2: Add actual data
        self.play(FadeOut(step1))
        step2 = Text("Bước 2:Gán giá trị cho data", font="Times New Roman").scale(0.7).next_to(title, DOWN)
        self.play(Write(step2))

        self.play(FadeOut(data_label))
        data_value = Text("42").scale(0.8).move_to(data_rect.get_center())
        data_rect.set_color(BLUE)
        self.play(Write(data_value))
        self.wait(1)

        # Step 3: Initialize pointer
        self.play(FadeOut(step2))
        step3 = Text("Bước 3:Gán giá trị nullptr cho con trỏ next", font="Times New Roman").scale(0.7).next_to(title, DOWN)
        self.play(Write(step3))

        self.play(FadeOut(pointer_label))
        pointer_value = Text("null").scale(0.6).move_to(pointer_rect.get_center())
        pointer_rect.set_color(BLUE)
        self.play(Write(pointer_value))
        self.wait(1)

        # C++ struct representation
        self.play(FadeOut(step3))
        struct_text = Text("Trong C++:", font="Times New Roman").scale(0.7).next_to(title, DOWN)
        self.play(Write(struct_text))
        self.wait(1)

        # Code representation using Text with larger box
        code_box = Rectangle(width=6.5, height=3, color=WHITE).move_to([0, -2, 0])

        code_line1 = Text("template <typename datatype>", font_size=28)
        code_line2 = Text("struct Node {", font_size=28)
        code_line3 = Text("    datatype data;", font_size=28)
        code_line4 = Text("    Node<datatype> *next;", font_size=28)
        code_line5 = Text("};", font_size=28)

        code_lines = VGroup(code_line1, code_line2, code_line3, code_line4, code_line5).arrange(DOWN, aligned_edge=LEFT)
        code_lines.move_to(code_box.get_center())

        self.play(Create(code_box), Write(code_lines))
        self.wait(2)

        # Final label
        node_complete = Text("~(￣▽￣)~*", color=GREEN).scale(0.8)
        node_complete.next_to(structure, DOWN, buff=0.5)
        self.play(Write(node_complete))

        self.wait(2)

class LinkedListScene(Scene):
    def construct(self):
        values = [1, 2, 3, 4, 5]
        nodes = []
        arrows = []
        pointer_values = ["0xA1", "0xB2", "0xC3", "0xD4", "0xE5", "null"]

        start_x = -4.5
        spacing = 2.5
        rect_width = 2
        rect_height = 1

        for i, val in enumerate(values):
            data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            data_text = Text(str(val)).scale(0.8).move_to(data_rect.get_center())
            data_part = VGroup(data_rect, data_text)

            pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            pointer_text = Text(pointer_values[i]).scale(0.6).move_to(pointer_rect.get_center())
            pointer_part = VGroup(pointer_rect, pointer_text)

            node = VGroup(data_part, pointer_part).arrange(RIGHT, buff=0)
            node.move_to([start_x + i * spacing, 0, 0])
            nodes.append(node)

        for i in range(len(nodes) - 1):
            arrow = Arrow(
                nodes[i][1].get_right(),
                nodes[i + 1][0].get_left(),
                buff=0.1, stroke_width=4, tip_length=0.5
            )
            arrows.append(arrow)

        head_label = Text("head").scale(0.7).next_to(nodes[0], UP)
        head_arrow = Arrow(head_label.get_bottom(), nodes[0].get_top(), buff=0.2, stroke_width=4, tip_length=0.5)

        null_text = Text("null").scale(0.8).next_to(nodes[-1], UP)
        null_arrow = Arrow(null_text.get_bottom(), nodes[-1][1].get_top(), buff=0.2, stroke_width=4, tip_length=0.5)

        self.play(Write(head_label), Create(head_arrow))
        for i, node in enumerate(nodes):
            self.play(FadeIn(node))
            if i < len(arrows):
                self.play(Create(arrows[i]))
        self.play(Write(null_text), Create(null_arrow))

        self.wait(1)


class PushFrontLinkedList(Scene):
    def construct(self):
        # Initial linked list setup (similar to LinkedListScene)
        values = [1, 2, 3, 4, 5]
        nodes = []
        arrows = []
        pointer_values = ["0xA1", "0xB2", "0xC3", "0xD4", "0xE5", "null"]

        # Further reduced parameters to fit screen better
        start_x = -3.8
        spacing = 1.8
        rect_width = 1.6
        rect_height = 0.9

        # Create initial linked list nodes
        for i, val in enumerate(values):
            data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            data_text = Text(str(val)).scale(0.7).move_to(data_rect.get_center())
            data_part = VGroup(data_rect, data_text)

            pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            pointer_text = Text(pointer_values[i]).scale(0.5).move_to(pointer_rect.get_center())
            pointer_part = VGroup(pointer_rect, pointer_text)

            node = VGroup(data_part, pointer_part).arrange(RIGHT, buff=0)
            node.move_to([start_x + i * spacing, 0, 0])
            nodes.append(node)

        # Create initial arrows - smaller and consistent
        arrow_style = {"buff": 0.02, "stroke_width": 1.5, "tip_length": 0.15}
        for i in range(len(nodes) - 1):
            arrow = Arrow(
                nodes[i][1].get_right(),
                nodes[i + 1][0].get_left(),
                **arrow_style
            )
            arrows.append(arrow)

        # Head pointer and null pointer - same style as other arrows
        head_label = Text("head").scale(0.6).next_to(nodes[0], UP, buff=0.1)
        head_arrow = Arrow(head_label.get_bottom(), nodes[0].get_top(), **arrow_style)

        null_text = Text("null").scale(0.6).next_to(nodes[-1], UP, buff=0.1)
        null_arrow = Arrow(null_text.get_bottom(), nodes[-1][1].get_top(), **arrow_style)

        # Display initial linked list
        initial_elements = [head_label, head_arrow, null_text, null_arrow] + nodes + arrows
        self.play(*[FadeIn(element) for element in initial_elements])
        self.wait(1)

        # Create title for the operation
        title = Text("Thêm 1 Node vào trước LinkedList", font="Times New Roman").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create new node to push front
        new_value = 0
        new_pointer = "0x90"

        data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=GREEN)
        data_text = Text(str(new_value)).scale(0.7).move_to(data_rect.get_center())
        data_part = VGroup(data_rect, data_text)

        pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=GREEN)
        pointer_text = Text(new_pointer).scale(0.5).move_to(pointer_rect.get_center())
        pointer_part = VGroup(pointer_rect, pointer_text)

        new_node = VGroup(data_part, pointer_part).arrange(RIGHT, buff=0)

        # Position the new node to the left of the scene
        new_node.move_to([start_x - spacing, 0, 0])

        # Create label for the new node
        new_node_label = Text("Node mới",font="Times New Roman").scale(0.6).next_to(new_node, DOWN, buff=0.1)

        # Show the creation of new node
        self.play(FadeIn(new_node), Write(new_node_label))
        self.wait(1)

        # Step 1: Move the existing list to the right
        self.play(
            *[node.animate.shift(RIGHT * spacing) for node in nodes],
            *[arrow.animate.shift(RIGHT * spacing) for arrow in arrows],
            null_text.animate.shift(RIGHT * spacing),
            null_arrow.animate.shift(RIGHT * spacing),
            FadeOut(new_node_label)
        )
        self.wait(1)

        # Step 2: Move the head pointer
        self.play(
            head_label.animate.next_to(new_node, UP, buff=0.1),
            FadeOut(head_arrow)
        )
        new_head_arrow = Arrow(head_label.get_bottom(), new_node.get_top(), **arrow_style)
        self.play(Create(new_head_arrow))
        self.wait(1)

        # Step 3: Connect new node to the old head (using same arrow style)
        new_to_old_arrow = Arrow(
            new_node[1].get_right(),
            nodes[0][0].get_left(),
            **arrow_style
        )
        self.play(Create(new_to_old_arrow))
        self.wait(1)

        # Step 4: Highlight the steps with annotations - positioned higher to avoid overlap
        step1 = Text("1. Tạo một Node mới", font="Times New Roman").scale(0.5).to_edge(DOWN, buff=1.5).shift(LEFT * 3.5)
        step2 = Text("2. Trỏ Node mới đến head cũ", font="Times New Roman").scale(0.5).next_to(step1, RIGHT, buff=0.5)
        step3 = Text("3. Cập nhật head mới",font="Times New Roman").scale(0.5).next_to(step2, RIGHT, buff=0.5)

        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))

        # Show time complexity - positioned lower to avoid overlap with step descriptions
        complexity = Text("Time Complexity: O(1)", color=YELLOW).scale(0.7).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(complexity))

        self.wait(2)


class PushBackLinkedList(Scene):
    def construct(self):
        # Initial linked list setup
        values = [1, 2, 3, 4, 5]
        nodes = []
        arrows = []
        pointer_values = ["0xA1", "0xB2", "0xC3", "0xD4", "0xE5", "null"]

        # Parameters to fit screen
        start_x = -3.8
        spacing = 1.8
        rect_width = 1.6
        rect_height = 0.9

        # Create initial linked list nodes
        for i, val in enumerate(values):
            data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            data_text = Text(str(val)).scale(0.7).move_to(data_rect.get_center())
            data_part = VGroup(data_rect, data_text)

            pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            pointer_text = Text(pointer_values[i]).scale(0.5).move_to(pointer_rect.get_center())
            pointer_part = VGroup(pointer_rect, pointer_text)

            node = VGroup(data_part, pointer_part).arrange(RIGHT, buff=0)
            node.move_to([start_x + i * spacing, 0, 0])
            nodes.append(node)

        # Create initial arrows
        arrow_style = {"buff": 0.02, "stroke_width": 1.5, "tip_length": 0.15}
        for i in range(len(nodes) - 1):
            arrow = Arrow(
                nodes[i][1].get_right(),
                nodes[i + 1][0].get_left(),
                **arrow_style
            )
            arrows.append(arrow)

        # Head pointer and null pointer
        head_label = Text("head").scale(0.6).next_to(nodes[0], UP, buff=0.1)
        head_arrow = Arrow(head_label.get_bottom(), nodes[0].get_top(), **arrow_style)

        null_text = Text("null").scale(0.6).next_to(nodes[-1], UP, buff=0.1)
        null_arrow = Arrow(null_text.get_bottom(), nodes[-1][1].get_top(), **arrow_style)

        # Display initial linked list
        initial_elements = [head_label, head_arrow, null_text, null_arrow] + nodes + arrows
        self.play(*[FadeIn(element) for element in initial_elements])
        self.wait(1)

        # Create title for the operation
        title = Text("Thêm Node vào sau linked list", font="Times New Roman").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create new node to push back
        new_value = 6
        new_pointer = "null"

        data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=GREEN)
        data_text = Text(str(new_value)).scale(0.7).move_to(data_rect.get_center())
        data_part = VGroup(data_rect, data_text)

        pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=GREEN)
        pointer_text = Text(new_pointer).scale(0.5).move_to(pointer_rect.get_center())
        pointer_part = VGroup(pointer_rect, pointer_text)

        new_node = VGroup(data_part, pointer_part).arrange(RIGHT, buff=0)

        # Position the new node to the right of the last node
        new_node.move_to([start_x + len(nodes) * spacing, 0, 0])

        # Create label for the new node
        new_node_label = Text("New Node").scale(0.6).next_to(new_node, DOWN, buff=0.1)

        # Show the creation of new node
        self.play(FadeIn(new_node), Write(new_node_label))
        self.wait(1)

        # Current pointer to simulate traversal
        curr_pointer = Text("finder").scale(0.6).next_to(nodes[0], DOWN, buff=0.1)
        curr_arrow = Arrow(curr_pointer.get_top(), nodes[0].get_bottom(), **arrow_style)
        self.play(Write(curr_pointer), Create(curr_arrow))

        # Traverse through each node
        for i in range(len(nodes) - 1):
            # Highlight current node
            self.play(nodes[i].animate.set_color(YELLOW))
            self.wait(0.5)

            # Check next pointer
            check_text = Text("next != null").scale(0.5).next_to(nodes[i], DOWN, buff=0.5)
            self.play(Write(check_text))
            self.wait(0.5)
            self.play(FadeOut(check_text))

            # Move to next node
            self.play(
                nodes[i].animate.set_color(BLUE),
                curr_pointer.animate.next_to(nodes[i + 1], DOWN, buff=0.1),
                FadeOut(curr_arrow)
            )
            curr_arrow = Arrow(curr_pointer.get_top(), nodes[i + 1].get_bottom(), **arrow_style)
            self.play(Create(curr_arrow))

        # Highlight the last node
        self.play(nodes[-1].animate.set_color(YELLOW))
        self.wait(0.5)

        # Check if this is the last node
        check_text = Text("next == null").scale(0.5).next_to(nodes[-1], DOWN, buff=0.5)
        self.play(Write(check_text))
        self.wait(0.5)
        self.play(FadeOut(check_text))

        # Step 1: Change the last node's next pointer
        found_text = Text("Tìm thấy node cuối!", font="Times New Roman").scale(0.6).next_to(nodes[-1], DOWN, buff=0.5)
        self.play(Write(found_text))
        self.wait(0.5)
        self.play(FadeOut(found_text))

        old_pointer_text = nodes[-1][1][1]
        new_address = "0xF6"
        updated_pointer = Text(new_address).scale(0.5).move_to(old_pointer_text.get_center())

        self.play(
            FadeOut(old_pointer_text),
            FadeIn(updated_pointer),
        )
        self.wait(1)

        # Step 2: Create an arrow from the last node to the new node
        last_to_new_arrow = Arrow(
            nodes[-1][1].get_right(),
            new_node[0].get_left(),
            **arrow_style
        )
        self.play(Create(last_to_new_arrow))
        self.wait(1)

        # Step 3: Move null pointer to the new node
        self.play(
            null_text.animate.next_to(new_node, UP, buff=0.1),
            FadeOut(null_arrow)
        )
        new_null_arrow = Arrow(null_text.get_bottom(), new_node[1].get_top(), **arrow_style)
        self.play(Create(new_null_arrow))
        self.wait(1)

        # Reset last node color and clean up traversal pointers
        self.play(
            nodes[-1].animate.set_color(BLUE),
            FadeOut(curr_pointer),
            FadeOut(curr_arrow),
            FadeOut(new_node_label)
        )
        self.wait(1)

        # Add explanation steps
        step1 = Text("1. Tạo Node mới", font="Times New Roman").scale(0.5).to_edge(DOWN, buff=1.5).shift(LEFT * 3.5)
        step2 = Text("2. Traverse đến Node cuối", font="Times New Roman").scale(0.5).next_to(step1, RIGHT, buff=0.5)
        step3 = Text("3. Nối node cuối với Node mới", font="Times New Roman").scale(0.5).next_to(step2, RIGHT, buff=0.5)

        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))

        # Show time complexity
        complexity = Text("Time Complexity: O(n), ",font="Times New Roman", color=YELLOW).scale(0.7).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(complexity))

        self.wait(2)


class PushBackLinkedListWithTail(Scene):
    def construct(self):
        # Initial linked list setup
        values = [1, 2, 3, 4, 5]
        nodes = []
        arrows = []
        pointer_values = ["0xA1", "0xB2", "0xC3", "0xD4", "0xE5", "null"]

        # Parameters to fit screen with better spacing
        start_x = -4.0
        spacing = 1.9
        rect_width = 1.6
        rect_height = 0.9

        # Create initial linked list nodes
        for i, val in enumerate(values):
            data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            data_text = Text(str(val)).scale(0.7).move_to(data_rect.get_center())
            data_part = VGroup(data_rect, data_text)

            pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            pointer_text = Text(pointer_values[i]).scale(0.5).move_to(pointer_rect.get_center())
            pointer_part = VGroup(pointer_rect, pointer_text)

            node = VGroup(data_part, pointer_part).arrange(RIGHT, buff=0)
            node.move_to([start_x + i * spacing, 0, 0])
            nodes.append(node)

        # Create initial arrows with reduced size
        arrow_style = {"buff": 0.02, "stroke_width": 1.5, "tip_length": 0.15}
        for i in range(len(nodes) - 1):
            arrow = Arrow(
                nodes[i][1].get_right(),
                nodes[i + 1][0].get_left(),
                **arrow_style
            )
            arrows.append(arrow)

        # Position pointers with better spacing to avoid overlap
        head_label = Text("head").scale(0.6).next_to(nodes[0], UP, buff=0.1)
        head_arrow = Arrow(head_label.get_bottom(), nodes[0].get_top(), **arrow_style)

        tail_label = Text("tail").scale(0.6)
        # Position tail at the last node
        tail_label.next_to(nodes[-1], UP, buff=0.1)
        tail_arrow = Arrow(tail_label.get_bottom(), nodes[-1].get_top(), **arrow_style)

        # Display initial linked list
        initial_elements = [head_label, head_arrow, tail_label, tail_arrow] + nodes + arrows
        self.play(*[FadeIn(element) for element in initial_elements])
        self.wait(1)

        # Create title for the operation
        title = Text("Thêm Node vào sau linked list (với con trỏ tail)", font="Times New Roman").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create new node to push back
        new_value = 6
        new_pointer = "null"

        data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=GREEN)
        data_text = Text(str(new_value)).scale(0.7).move_to(data_rect.get_center())
        data_part = VGroup(data_rect, data_text)

        pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=GREEN)
        pointer_text = Text(new_pointer).scale(0.5).move_to(pointer_rect.get_center())
        pointer_part = VGroup(pointer_rect, pointer_text)

        new_node = VGroup(data_part, pointer_part).arrange(RIGHT, buff=0)

        # Position the new node to the right of the last node
        new_node.move_to([start_x + len(nodes) * spacing, 0, 0])

        # Create label for the new node
        new_node_label = Text("New Node").scale(0.6).next_to(new_node, DOWN, buff=0.1)

        # Show the creation of new node
        self.play(FadeIn(new_node), Write(new_node_label))
        self.wait(1)

        # Step 1: Highlight the tail node
        self.play(nodes[-1].animate.set_color(YELLOW))
        self.wait(1)

        # Step 2: Change the last node's next pointer
        old_pointer_text = nodes[-1][1][1]
        new_address = "0xF6"
        updated_pointer = Text(new_address).scale(0.5).move_to(old_pointer_text.get_center())

        self.play(
            FadeOut(old_pointer_text),
            FadeIn(updated_pointer),
        )
        self.wait(1)

        # Step 3: Create an arrow from the last node to the new node
        last_to_new_arrow = Arrow(
            nodes[-1][1].get_right(),
            new_node[0].get_left(),
            **arrow_style
        )
        self.play(Create(last_to_new_arrow))
        self.wait(1)

        # Step 4: Move tail pointer to the new node
        self.play(
            tail_label.animate.next_to(new_node, UP, buff=0.1),
            FadeOut(tail_arrow)
        )

        new_tail_arrow = Arrow(tail_label.get_bottom(), new_node.get_top(), **arrow_style)
        self.play(Create(new_tail_arrow))
        self.wait(1)

        # Reset last node color and remove new node label
        self.play(
            nodes[-1].animate.set_color(BLUE),
            FadeOut(new_node_label)
        )
        self.wait(1)

        # Add explanation steps
        step1 = Text("1. Tạo Node mới", font="Times New Roman").scale(0.5).to_edge(DOWN, buff=1.5).shift(LEFT * 3.5)
        step2 = Text("2. Trỏ tail đến Node mới", font="Times New Roman").scale(0.5).next_to(step1, RIGHT, buff=0.5)
        step3 = Text("3. Cập nhật tail", font="Times New Roman").scale(0.5).next_to(step2, RIGHT, buff=0.5)

        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))

        # Show time complexity
        complexity = Text("Time Complexity: O(1)", color=YELLOW).scale(0.7).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(complexity))

        self.wait(2)
class SearchLinkedList(Scene):
    def construct(self):
        # Initial linked list setup
        values = [3, 1, 7, 4, 2]
        target_value = 7  # Value to search for
        nodes = []
        arrows = []
        pointer_values = ["0xA1", "0xB2", "0xC3", "0xD4", "0xE5", "null"]

        # Parameters to fit screen
        start_x = -4.0
        spacing = 1.9
        rect_width = 1.6
        rect_height = 0.9

        # Create title for the operation
        title = Text("Tìm kiếm giá trị trong LinkedList", font="Times New Roman").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create initial linked list nodes
        for i, val in enumerate(values):
            data_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            data_text = Text(str(val), font="Times New Roman").scale(0.7).move_to(data_rect.get_center())
            data_part = VGroup(data_rect, data_text)

            pointer_rect = Rectangle(width=rect_width / 2, height=rect_height, color=BLUE)
            pointer_text = Text(pointer_values[i], font="Times New Roman").scale(0.5).move_to(pointer_rect.get_center())
            pointer_part = VGroup(pointer_rect, pointer_text)

            node = VGroup(data_part, pointer_part).arrange(RIGHT, buff=0)
            node.move_to([start_x + i * spacing, 0, 0])
            nodes.append(node)

        # Create arrows with consistent style
        arrow_style = {"buff": 0.02, "stroke_width": 1.5, "tip_length": 0.15}
        for i in range(len(nodes) - 1):
            arrow = Arrow(
                nodes[i][1].get_right(),
                nodes[i + 1][0].get_left(),
                **arrow_style
            )
            arrows.append(arrow)

        # Head pointer
        head_label = Text("head", font="Times New Roman").scale(0.6).next_to(nodes[0], UP, buff=0.1)
        head_arrow = Arrow(head_label.get_bottom(), nodes[0].get_top(), **arrow_style)

        # Display initial linked list
        initial_elements = [head_label, head_arrow] + nodes + arrows
        self.play(*[FadeIn(element) for element in initial_elements])
        self.wait(1)

        # Show search target
        search_text = Text(f"Tìm giá trị: {target_value}", font="Times New Roman").scale(0.7)
        search_text.next_to(title, DOWN, buff=0.3)
        self.play(Write(search_text))
        self.wait(1)

        # Create current pointer for traversal
        current_pointer = Text("current", font="Times New Roman").scale(0.6)
        current_pointer.next_to(nodes[0], DOWN, buff=0.3)
        current_arrow = Arrow(current_pointer.get_top(), nodes[0].get_bottom(), **arrow_style)
        self.play(Write(current_pointer), Create(current_arrow))
        self.wait(1)

        # Pseudocode for the search algorithm
        code_box = Rectangle(width=6, height=2.5, color=WHITE).to_edge(DOWN, buff=0.5)

        code_line1 = Text("Node* search(int value) {", font="Courier New", font_size=24)
        code_line2 = Text("    Node* current = head;", font="Courier New", font_size=24)
        code_line3 = Text("    while (current != nullptr) {", font="Courier New", font_size=24)
        code_line4 = Text("        if (current->data == value) return current;", font="Courier New", font_size=24)
        code_line5 = Text("        current = current->next;", font="Courier New", font_size=24)
        code_line6 = Text("    }", font="Courier New", font_size=24)
        code_line7 = Text("    return nullptr; // Not found", font="Courier New", font_size=24)
        code_line8 = Text("}", font="Courier New", font_size=24)

        code_lines = VGroup(code_line1, code_line2, code_line3, code_line4,
                           code_line5, code_line6, code_line7, code_line8)
        code_lines.arrange(DOWN, aligned_edge=LEFT)
        code_lines.scale(0.6).move_to(code_box.get_center())

        self.play(Create(code_box), Write(code_lines))
        self.wait(1)

        # Traverse the list looking for the target value
        for i, node in enumerate(nodes):
            # Highlight the current node being checked
            self.play(node.animate.set_color(YELLOW))
            self.wait(0.5)

            # Highlight the comparison in the code
            self.play(code_line4.animate.set_color(YELLOW))
            self.wait(0.5)

            # Check if current node has the target value
            check_text = Text(f"current->data == {target_value}?", font="Times New Roman").scale(0.6)
            check_text.next_to(node, UP, buff=0.4)
            self.play(Write(check_text))
            self.wait(1)

            # If this is the target node
            if values[i] == target_value:
                # Found the value!
                found_text = Text("Giá trị được tìm thấy!", font="Times New Roman", color=GREEN).scale(0.7)
                found_text.next_to(check_text, UP, buff=0.2)
                self.play(
                    Write(found_text),
                    node.animate.set_color(GREEN),
                    FadeOut(check_text)
                )

                # Draw return arrow and value
                return_arrow = Arrow(start=LEFT, end=RIGHT, color=GREEN).scale(0.5)
                return_arrow.next_to(code_line4, RIGHT, buff=0.1)
                return_label = Text("return", font="Times New Roman", color=GREEN).scale(0.5)
                return_label.next_to(return_arrow, UP, buff=0.1)
                self.play(
                    Create(return_arrow),
                    Write(return_label),
                    code_line4.animate.set_color(GREEN)
                )

                self.wait(1)
                break
            else:
                # Not found in this node, move to next
                self.play(
                    node.animate.set_color(RED),
                    FadeOut(check_text),
                    code_line4.animate.set_color(WHITE)
                )

                # Highlight moving to the next node in the code
                self.play(code_line5.animate.set_color(YELLOW))
                self.wait(0.5)
                self.play(code_line5.animate.set_color(WHITE))

                # Move current pointer to next node if not at the end
                if i < len(nodes) - 1:
                    self.play(
                        current_pointer.animate.next_to(nodes[i+1], DOWN, buff=0.3),
                        FadeOut(current_arrow)
                    )
                    current_arrow = Arrow(current_pointer.get_top(), nodes[i+1].get_bottom(), **arrow_style)
                    self.play(Create(current_arrow))
                    self.wait(0.5)

                    # Reset node color
                    self.play(node.animate.set_color(BLUE))
                else:
                    # Value not found in the list
                    not_found = Text("Giá trị không tồn tại!", font="Times New Roman", color=RED).scale(0.7)
                    not_found.next_to(node, UP, buff=0.4)

                    # Highlight the return null in the code
                    self.play(
                        Write(not_found),
                        code_line7.animate.set_color(RED)
                    )

                    # Draw return arrow for not found case
                    return_arrow = Arrow(start=LEFT, end=RIGHT, color=RED).scale(0.5)
                    return_arrow.next_to(code_line7, RIGHT, buff=0.1)
                    return_label = Text("return", font="Times New Roman", color=RED).scale(0.5)
                    return_label.next_to(return_arrow, UP, buff=0.1)
                    self.play(
                        Create(return_arrow),
                        Write(return_label)
                    )

                    self.wait(1)

        # Show time complexity
        complexity = Text("Time Complexity: O(n)", font="Times New Roman", color=YELLOW).scale(0.7)
        complexity.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(complexity))

        self.wait(2)