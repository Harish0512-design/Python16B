# Implement a Browser History (Back & Forward Buttons)
# When browsing pages, you can go back and forward — both are operations at the ends of a list.
# Use Case: Efficiently manage undo/redo or back/forward systems in apps.

from collections import deque

class BrowserHistory:
    def __init__(self):
        self.forward_stack = deque()
        self.backward_stack = deque()
        self.current = None

    def visit(self, url):
        """
            checks if current window as url.
            if it has the url then put that url in backward_stack()
            and put the url in current window.
            and clears the forward stack.
        """
        if self.current:
            self.backward_stack.append(self.current)

        self.current = url
        self.forward_stack.clear()

        print(self.current)

    def go_back(self):
        """
            push current url to forward_stack
            current_url = backward_stack.pop()
        """
        if self.backward_stack:
            self.forward_stack.appendleft(self.current)
            self.current = self.backward_stack.pop()
        
        print(self.current)

    def go_forward(self):
        """
            put current url as backward_stack last item
            current = forward_stack.popleft()(first_item)
        """
        if self.forward_stack:
            self.backward_stack.append(self.current)
            self.current = self.forward_stack.popleft()

        print(self.current)

if __name__ == "__main__":
    bh = BrowserHistory()
    bh.visit("https:www.google.com")
    bh.visit("https:www.youtube.com")
    bh.visit("https:www.instagram.com")

    bh.go_forward()
    bh.go_back()
    bh.go_forward()
