import json

import pygame as pg

from source.Constants import *
from source.Interface.Buttons import Button
from source.Interface.TextInput import TextInput
from source.Inventory.Items.ItemModel import DB, ItemsRank1, ItemsRank2, ItemsRank3, ItemsBlocked


class ItemsCreatorInterface:
    font1 = pg.font.Font("resource/fonts/EightBits.ttf", 30)
    font2 = pygame.font.Font('resource/fonts/EightBits.ttf', 90)

    def __init__(self, screen) -> None:
        super().__init__()
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.background.fill("white")

        self.text_id = self.font1.render("id:", True, (0, 0, 0))
        self.input_id = TextInput(60, 60, w=100, f_s=30, b_w=2)
        self.text_name = self.font1.render("name:", True, (0, 0, 0))
        self.input_name = TextInput(60, 130, w=100, f_s=30, b_w=2)
        self.text_description = self.font1.render("description:", True, (0, 0, 0))
        self.input_description = TextInput(210, 200, w=400, f_s=30, b_w=2)
        self.text_rank = self.font1.render("rank:", True, (0, 0, 0))
        self.input_rank = TextInput(30, 280, w=40, f_s=30, b_w=2)

        self.text_renewal_plus = self.font1.render("renewal_plus:", True, (0, 0, 0))
        self.input_renewal_plus_1 = TextInput(600, 60, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_2 = TextInput(600, 100, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_3 = TextInput(600, 140, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_4 = TextInput(600, 180, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_5 = TextInput(600, 220, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_6 = TextInput(600, 260, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_7 = TextInput(600, 300, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_8 = TextInput(600, 340, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_9 = TextInput(600, 380, w=200, f_s=30, b_w=2)
        self.input_renewal_plus_10 = TextInput(600, 420, w=200, f_s=30, b_w=2)

        self.text_renewal_multiply = self.font1.render("renewal_multiply:", True, (0, 0, 0))
        self.input_renewal_multiply_1 = TextInput(820, 60, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_2 = TextInput(820, 100, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_3 = TextInput(820, 140, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_4 = TextInput(820, 180, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_5 = TextInput(820, 220, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_6 = TextInput(820, 260, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_7 = TextInput(820, 300, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_8 = TextInput(820, 340, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_9 = TextInput(820, 380, w=200, f_s=30, b_w=2)
        self.input_renewal_multiply_10 = TextInput(820, 420, w=200, f_s=30, b_w=2)

        self.text_renewal_super = self.font1.render("renewal_super:", True, (0, 0, 0))

        self.input_renewal_super_1 = TextInput(1040, 60, w=200, f_s=30, b_w=2)
        self.input_renewal_super_2 = TextInput(1040, 100, w=200, f_s=30, b_w=2)
        self.input_renewal_super_3 = TextInput(1040, 140, w=200, f_s=30, b_w=2)
        self.input_renewal_super_4 = TextInput(1040, 180, w=200, f_s=30, b_w=2)
        self.input_renewal_super_5 = TextInput(1040, 220, w=200, f_s=30, b_w=2)
        self.input_renewal_super_6 = TextInput(1040, 260, w=200, f_s=30, b_w=2)
        self.input_renewal_super_7 = TextInput(1040, 300, w=200, f_s=30, b_w=2)
        self.input_renewal_super_8 = TextInput(1040, 340, w=200, f_s=30, b_w=2)
        self.input_renewal_super_9 = TextInput(1040, 380, w=200, f_s=30, b_w=2)
        self.input_renewal_super_10 = TextInput(1040, 420, w=200, f_s=30, b_w=2)

        self.text_code = self.font1.render("code:", True, (0, 0, 0))
        self.input_code = TextInput(1430, 60, w=500, f_s=30, b_w=2)

        self.button_exit = Button("Exit", np.array([180, HEIGHT - 100]), np.array([150, 50]), font=self.font2)
        self.button_compile = Button("Compile", np.array([WIDTH - 180, HEIGHT - 100]), np.array([150, 50]),
                                     font=self.font2)

    def compile(self):
        try:
            id_ = self.input_id.get()
            name = self.input_name.get()
            description = self.input_description.get()
            rank = int(self.input_rank.get())
            blocking = True
            renewal_plus = {}
            renewal_multiply = {}
            renewal_super = {}
            code = self.input_code.get()

            if self.input_renewal_plus_1.get() != "":
                name_, value = self.input_renewal_plus_1.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_2.get() != "":
                name_, value = self.input_renewal_plus_2.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_3.get() != "":
                name_, value = self.input_renewal_plus_3.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_4.get() != "":
                name_, value = self.input_renewal_plus_4.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_5.get() != "":
                name_, value = self.input_renewal_plus_5.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_6.get() != "":
                name_, value = self.input_renewal_plus_6.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_7.get() != "":
                name_, value = self.input_renewal_plus_7.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_8.get() != "":
                name_, value = self.input_renewal_plus_8.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_9.get() != "":
                name_, value = self.input_renewal_plus_9.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_plus_10.get() != "":
                name_, value = self.input_renewal_plus_10.get().split()
                value = int(value)
                renewal_plus[name_] = value

            if self.input_renewal_multiply_1.get() != "":
                name_, value = self.input_renewal_multiply_1.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_2.get() != "":
                name_, value = self.input_renewal_multiply_2.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_3.get() != "":
                name_, value = self.input_renewal_multiply_3.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_4.get() != "":
                name_, value = self.input_renewal_multiply_4.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_5.get() != "":
                name_, value = self.input_renewal_multiply_5.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_6.get() != "":
                name_, value = self.input_renewal_multiply_6.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_7.get() != "":
                name_, value = self.input_renewal_multiply_7.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_8.get() != "":
                name_, value = self.input_renewal_multiply_8.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_9.get() != "":
                name_, value = self.input_renewal_multiply_9.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_multiply_10.get() != "":
                name_, value = self.input_renewal_multiply_10.get().split()
                value = int(value)
                renewal_multiply[name_] = value

            if self.input_renewal_super_1.get() != "":
                name_, value = self.input_renewal_super_1.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_2.get() != "":
                name_, value = self.input_renewal_super_2.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_3.get() != "":
                name_, value = self.input_renewal_super_3.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_4.get() != "":
                name_, value = self.input_renewal_super_4.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_5.get() != "":
                name_, value = self.input_renewal_super_5.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_6.get() != "":
                name_, value = self.input_renewal_super_6.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_7.get() != "":
                name_, value = self.input_renewal_super_7.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_8.get() != "":
                name_, value = self.input_renewal_super_8.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_9.get() != "":
                name_, value = self.input_renewal_super_9.get().split()
                value = int(value)
                renewal_super[name_] = value

            if self.input_renewal_super_10.get() != "":
                name_, value = self.input_renewal_super_10.get().split()
                value = int(value)
                renewal_super[name_] = value

            with DB.atomic():
                if rank == -1:
                    ItemsBlocked.create(id=id_,
                                        name=name,
                                        description=description,
                                        renewal_plus=json.dumps(renewal_plus),
                                        renewal_multiply=json.dumps(renewal_multiply),
                                        renewal_super=json.dumps(renewal_super),
                                        blocking=blocking,
                                        code=code)
                if rank == 1:
                    ItemsRank1.create(id=id_,
                                      name=name,
                                      description=description,
                                      renewal_plus=json.dumps(renewal_plus),
                                      renewal_multiply=json.dumps(renewal_multiply),
                                      renewal_super=json.dumps(renewal_super),
                                      code=code)
                if rank == 2:
                    ItemsRank2.create(id=id_,
                                      name=name,
                                      description=description,
                                      renewal_plus=json.dumps(renewal_plus),
                                      renewal_multiply=json.dumps(renewal_multiply),
                                      renewal_super=json.dumps(renewal_super),
                                      code=code)
                if rank == 3:
                    ItemsRank3.create(id=id_,
                                      name=name,
                                      description=description,
                                      renewal_plus=json.dumps(renewal_plus),
                                      renewal_multiply=json.dumps(renewal_multiply),
                                      renewal_super=json.dumps(renewal_super),
                                      code=code)

            print("sus")
        except Exception as e:
            print(e)
            print("Not Sus")
        finally:
            self.clear()

    def clear(self):
        self.input_renewal_plus_1.set("")
        self.input_renewal_plus_2.set("")
        self.input_renewal_plus_3.set("")
        self.input_renewal_plus_4.set("")
        self.input_renewal_plus_5.set("")
        self.input_renewal_plus_6.set("")
        self.input_renewal_plus_7.set("")
        self.input_renewal_plus_8.set("")
        self.input_renewal_plus_9.set("")
        self.input_renewal_plus_10.set("")
        self.input_renewal_multiply_1.set("")
        self.input_renewal_multiply_2.set("")
        self.input_renewal_multiply_3.set("")
        self.input_renewal_multiply_4.set("")
        self.input_renewal_multiply_5.set("")
        self.input_renewal_multiply_6.set("")
        self.input_renewal_multiply_7.set("")
        self.input_renewal_multiply_8.set("")
        self.input_renewal_multiply_9.set("")
        self.input_renewal_multiply_10.set("")
        self.input_renewal_super_1.set("")
        self.input_renewal_super_2.set("")
        self.input_renewal_super_3.set("")
        self.input_renewal_super_4.set("")
        self.input_renewal_super_5.set("")
        self.input_renewal_super_6.set("")
        self.input_renewal_super_7.set("")
        self.input_renewal_super_8.set("")
        self.input_renewal_super_9.set("")
        self.input_renewal_super_10.set("")

        self.input_code.set("")
        self.input_name.set("")
        self.input_rank.set("")
        self.input_description.set("")
        self.input_id.set("")

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text_id, (10, 10))
        self.input_id.draw(self.screen)
        self.screen.blit(self.text_name, (10, 80))
        self.input_name.draw(self.screen)
        self.screen.blit(self.text_description, (10, 150))
        self.input_description.draw(self.screen)
        self.screen.blit(self.text_rank, (10, 220))
        self.input_rank.draw(self.screen)

        self.screen.blit(self.text_renewal_plus, (500, 10))

        self.input_renewal_plus_1.draw(self.screen)
        self.input_renewal_plus_2.draw(self.screen)
        self.input_renewal_plus_3.draw(self.screen)
        self.input_renewal_plus_4.draw(self.screen)
        self.input_renewal_plus_5.draw(self.screen)
        self.input_renewal_plus_6.draw(self.screen)
        self.input_renewal_plus_7.draw(self.screen)
        self.input_renewal_plus_8.draw(self.screen)
        self.input_renewal_plus_9.draw(self.screen)
        self.input_renewal_plus_10.draw(self.screen)

        self.screen.blit(self.text_renewal_multiply, (720, 10))

        self.input_renewal_multiply_1.draw(self.screen)
        self.input_renewal_multiply_2.draw(self.screen)
        self.input_renewal_multiply_3.draw(self.screen)
        self.input_renewal_multiply_4.draw(self.screen)
        self.input_renewal_multiply_5.draw(self.screen)
        self.input_renewal_multiply_6.draw(self.screen)
        self.input_renewal_multiply_7.draw(self.screen)
        self.input_renewal_multiply_8.draw(self.screen)
        self.input_renewal_multiply_9.draw(self.screen)
        self.input_renewal_multiply_10.draw(self.screen)

        self.screen.blit(self.text_renewal_super, (940, 10))

        self.input_renewal_super_1.draw(self.screen)
        self.input_renewal_super_2.draw(self.screen)
        self.input_renewal_super_3.draw(self.screen)
        self.input_renewal_super_4.draw(self.screen)
        self.input_renewal_super_5.draw(self.screen)
        self.input_renewal_super_6.draw(self.screen)
        self.input_renewal_super_7.draw(self.screen)
        self.input_renewal_super_8.draw(self.screen)
        self.input_renewal_super_9.draw(self.screen)
        self.input_renewal_super_10.draw(self.screen)

        self.screen.blit(self.text_code, (1180, 10))

        self.input_code.draw(self.screen)
        self.button_exit.draw(self.screen)
        self.button_compile.draw(self.screen)

    def update(self):
        self.input_id.update()
        self.input_name.update()
        self.input_description.update()
        self.input_rank.update()

        self.input_renewal_plus_1.update()
        self.input_renewal_plus_2.update()
        self.input_renewal_plus_3.update()
        self.input_renewal_plus_4.update()
        self.input_renewal_plus_5.update()
        self.input_renewal_plus_6.update()
        self.input_renewal_plus_7.update()
        self.input_renewal_plus_8.update()
        self.input_renewal_plus_9.update()
        self.input_renewal_plus_10.update()

        self.input_renewal_multiply_1.update()
        self.input_renewal_multiply_2.update()
        self.input_renewal_multiply_3.update()
        self.input_renewal_multiply_4.update()
        self.input_renewal_multiply_5.update()
        self.input_renewal_multiply_6.update()
        self.input_renewal_multiply_7.update()
        self.input_renewal_multiply_8.update()
        self.input_renewal_multiply_9.update()
        self.input_renewal_multiply_10.update()

        self.input_renewal_super_1.update()
        self.input_renewal_super_2.update()
        self.input_renewal_super_3.update()
        self.input_renewal_super_4.update()
        self.input_renewal_super_5.update()
        self.input_renewal_super_6.update()
        self.input_renewal_super_7.update()
        self.input_renewal_super_8.update()
        self.input_renewal_super_9.update()
        self.input_renewal_super_10.update()

        self.input_code.update()

    def check_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button_compile.update(np.array(pg.mouse.get_pos())):
                    self.compile()

        self.input_id.handle_event(event)
        self.input_name.handle_event(event)
        self.input_description.handle_event(event)
        self.input_rank.handle_event(event)

        self.input_renewal_plus_1.handle_event(event)
        self.input_renewal_plus_2.handle_event(event)
        self.input_renewal_plus_3.handle_event(event)
        self.input_renewal_plus_4.handle_event(event)
        self.input_renewal_plus_5.handle_event(event)
        self.input_renewal_plus_6.handle_event(event)
        self.input_renewal_plus_7.handle_event(event)
        self.input_renewal_plus_8.handle_event(event)
        self.input_renewal_plus_9.handle_event(event)
        self.input_renewal_plus_10.handle_event(event)

        self.input_renewal_multiply_1.handle_event(event)
        self.input_renewal_multiply_2.handle_event(event)
        self.input_renewal_multiply_3.handle_event(event)
        self.input_renewal_multiply_4.handle_event(event)
        self.input_renewal_multiply_5.handle_event(event)
        self.input_renewal_multiply_6.handle_event(event)
        self.input_renewal_multiply_7.handle_event(event)
        self.input_renewal_multiply_8.handle_event(event)
        self.input_renewal_multiply_9.handle_event(event)
        self.input_renewal_multiply_10.handle_event(event)

        self.input_renewal_super_1.handle_event(event)
        self.input_renewal_super_2.handle_event(event)
        self.input_renewal_super_3.handle_event(event)
        self.input_renewal_super_4.handle_event(event)
        self.input_renewal_super_5.handle_event(event)
        self.input_renewal_super_6.handle_event(event)
        self.input_renewal_super_7.handle_event(event)
        self.input_renewal_super_8.handle_event(event)
        self.input_renewal_super_9.handle_event(event)
        self.input_renewal_super_10.handle_event(event)

        self.input_code.handle_event(event)
