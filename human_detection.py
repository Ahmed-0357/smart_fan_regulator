import cv2


class HumanCounter:
    """count number of humans in certain location using webcamp/CCTV
    """

    # get class names
    class_file = "./ssd mobilenet v3/coco.names"
    with open(class_file, "r") as f:
        class_names = f.read().splitlines()

    # get model architecture and weights (ssd mobilenet v3)
    config_path = "./ssd mobilenet v3/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    weights_path = "./ssd mobilenet v3/frozen_inference_graph.pb"

    @staticmethod
    def draw_annotate(img, text, bbox):
        """draw bbox and annotate class name & prediction accuracy

        Args:
            img (numpy ndarray): video frame
            text (str):  class name & prediction accuracy
            bbox (tuple): bounding box data (x, y, width, height)
        """
        colors = [(255, 255, 255), (255, 0, 255)]
        # put text in rectangle
        ox, oy = (bbox[0]+9, bbox[1]-12)
        (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, 1.5, 3)

        x1, y1, x2, y2 = ox - 10, oy + 10, ox + w + 10, oy - h - 10

        cv2.rectangle(img, (x1, y1), (x2, y2), colors[1], cv2.FILLED)
        cv2.putText(img, text, (ox, oy), cv2.FONT_HERSHEY_PLAIN,
                    1.5, colors[0], 3)

        # draw bbox
        cv2.rectangle(img, bbox, (255, 0, 255), 2)

    def run_count(self, child_conn):
        """count number of human in a location and send it to main.py

        Args:
            child_conn (object ): pipe child connection
        """

        # create ssd mobilenet v3 detection model
        net = cv2.dnn_DetectionModel(self.weights_path, self.config_path)
        net.setInputSize(120, 120)  # or 320, 120
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        # detect number of human at each frame
        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            class_ids, prediction_confs, bboxes = net.detect(
                img, confThreshold=0.6)  # detection threshold is 60%

            human_count = 0
            if len(class_ids) != 0:
                for class_id, confidence, box in zip(class_ids.flatten(), prediction_confs.flatten(), bboxes):
                    if class_id == 1:  # only detect a person
                        human_count += 1

                        HumanCounter.draw_annotate(
                            img, f'{self.class_names[class_id-1].upper()} - {int(confidence*100)}%', box)

            # pass human count value to main.py
            child_conn.value = human_count

            cv2.imshow('Camera', img)
            if cv2.waitKey(5) & 0xFF == ord('k'):
                break

        cap.release()
