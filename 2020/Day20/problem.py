import copy

def decode(input_text):
    with open(input_text) as f:
        input_lines = [line.strip() for line in f]
        photos = []

        for i in range(0, len(input_lines), 12):
            ID = input_lines[i][5:9]
            image = []
            for x in range(1,11):
                image.append(copy.deepcopy(list(input_lines[i + x])))

            photo = Tile_Image(ID, image)
            photos.append(photo)

        return photos


class Tile_Image():

    def __init__(self, ID, image):
        self.ID = ID
        # Edges defined in counter clockwise manner S.T the first element will always the leftmost object relative to orientation
        # i.e North Face --> from left to right || East Face --> Top to bottom || South Face --> right to left || West Face --> Bottom to top
        edges = [copy.deepcopy(image[0]), copy.deepcopy([image[x][-1] for x in range(len(image))]), copy.deepcopy(image[-1]), copy.deepcopy([image[x][0] for x in range(len(image))])]
        edges[2].reverse()
        edges[3].reverse()
        self.edges = edges
        self.image = image


        # Orientation is integer from [0, 7] representing each use of possible_rotations loop
        self.orientation = 0
        self.neighbor_IDs = []

    def display(self, edges):
        print(self.ID)
        for line in self.image:
            print(line)

        if edges == True:
            print()
            for edge in self.edges:
                print(edge)

    def rotate_clockwise(self):
        rotated_image = [[] for x in range(len(self.image))]
        for row in copy.deepcopy(self.image):
            for index in range(len(row)):
                rotated_image[index].insert(0, row[index])

        self.image = rotated_image

    def rotate_clockwise_edge(self):
        list = []
        for i in range(len(self.edges)):
            list.append(copy.deepcopy(self.edges[(i - 1) % 4]))

        self.edges = list

    def flip_edge(self):
        for edge in self.edges:
            edge.reverse()

        top = copy.deepcopy(self.edges[0])
        self.edges[0] = copy.deepcopy(self.edges[2])
        self.edges[2] = top

    def possible_rotations(self, *args):
        # args[0] --> orientation boolean

        posb_combos = []
        i = 0
        while i < 8:
            posb_combos.append(copy.deepcopy(self.edges))
            if i == 3:
                self.flip_edge()
            else:
                self.rotate_clockwise_edge()
                self.rotate_clockwise()

            if len(args) > 0:
                if args[0] and i == self.orientation:
                    return "Rotation completed"
            i+=1

        return posb_combos


    def count_matching_edges(self, other_list):
        self_posb_edges = self.possible_rotations()
        max = 0
        count = 0
        neighbor_IDs = []

        for self_orientation in self_posb_edges:

            if count > max:
                max = count
                cnst_neighbor_IDs = neighbor_IDs

            neighbor_IDs.clear()
            count = 0

            for other in other_list:
                if self.ID != other.ID:
                    prev_count = count
                    other_posb_edges = other.possible_rotations()

                    for other_rot in other_posb_edges:
                        for edge_index in range(len(self_orientation)):
                            if self_orientation[edge_index] in other_rot:
                                count+=1
                                neighbor_IDs.append(other.ID)
                                break
                        if count == prev_count + 1:
                            break

        self.neighbor_IDs = cnst_neighbor_IDs
        return max

class Completed_Image():

    def __init__(self, side_length, tile_list):
        self.side_length = side_length
        self.tile_list = tile_list
        self.image = [["" for x in range(side_length)] for y in range(side_length)]

    # Assume each tile in tile_list has neighbor_IDs with ordered ID --> (0, ID), (1, ID) etc.
    def sort_IDs(self):
        for tile in self.tile_list:
            tile.neighbor_IDs = sort_tuple(tile.neighbor_IDs)

    def construct_img(self):
        # find the top-left corner tile
        for tile in self.tile_list:
            if len(tile.neighbor_IDs) == 2 and tile.neighbor_IDs[0][1] == 1 and tile.neighbor_IDs[1][1] == 2:
                init_tile = tile

        self.image[0][0] = init_tile
        k = 0
        i = 0
        j = 0

        # Top left corner only corner that doesnt work for loop so manual iteration
        init_tile = self.find_tile(init_tile.neighbor_IDs[0][0])
        j += 1
        k += 1
        self.image[i][j] = init_tile

        while k < self.side_length ** 2:
            if init_tile.neighbor_IDs[1][1] == 1:
                init_tile = self.find_tile(init_tile.neighbor_IDs[1][0])
                j += 1
            elif init_tile.neighbor_IDs[-2][1] == 2:
                init_tile = self.find_tile(init_tile.neighbor_IDs[-2][0])
                i += 1
            elif init_tile.neighbor_IDs[-1][1] == 3:
                init_tile = self.find_tile(init_tile.neighbor_IDs[-1][0])
                j -= 1
            else:
                print("PROBLEM!!!!")

            self.image[i][j] = init_tile
            k += 1

    def find_tile(self, tile_ID):
        for tile in self.tile_list:
            if tile.ID == tile_ID:
                return tile

def sort_tuple(tup):
    return(sorted(tup, key = lambda x: x[1]))

if __name__ == "__main__":
    photos = decode("test.txt")
    #photos[0].display(False)
    for photo in photos:
        #photo.rotate_clockwise()
        #photo.display(False)
        photo.count_matching_edges(photos)
        #if len(photo.neighbor_IDs) == 2:
        print(photo.ID)
        print(photo.neighbor_IDs)

    image = Completed_Image(3, photos)
    #image.sort_IDs()
    #image.construct_img()
    #for tile in image.tile_list:
        #print(tile.ID)
        #print(tile.neighbor_IDs)


    #image = Completed_Image(12, photos)
