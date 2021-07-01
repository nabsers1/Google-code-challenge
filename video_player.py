"""A video player class."""

from .video_library import VideoLibrary
import random
from collections import defaultdict



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = []
        self.stopped = False
        self.paused = False
        self.paused_video = []
        self.id_list = list(self._video_library._videos.keys())
        self.title_list = [t.title for t in self._video_library.get_all_videos()]
        self.name_dict = {self.id_list[i]:self.title_list[i] for i in range(len(self.id_list))}
        self.rev_name_dict = {v:k for k,v in self.name_dict.items()}
        self.playlist_names = []
        self.playlists = defaultdict(list)


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for video in sorted(self._video_library.get_all_videos(),key = lambda x:x.title):
            print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        in_list = False
        while not in_list:
            if len(self.current_video) > 0 and video_id in self.id_list and not self.stopped:
                print(f'Stopping video: {self.current_video[-1]}')
                print(f'Playing video: {self.name_dict[video_id]}')
                self.current_video.append(self.name_dict[video_id])
                self.paused = False
                break

            elif video_id in self.id_list and (len(self.current_video) < 1 or self.stopped):
                in_list = True
                print(f'Playing video: {self.name_dict[video_id]}')
                self.current_video.append(self.name_dict[video_id])
                self.stopped = False
                self.paused = False

            else:
                print('Cannot play video: Video does not exist')
                break
    def stop_video(self):
        """Stops the current video."""

        if  self.stopped == True or len(self.current_video) < 1:
            print('Cannot stop video: No video is currently playing')
           
        else:
            print(f'Stopping video: {self.current_video[-1]}')
            self.stopped = True


    def play_random_video(self):
        """Plays a random video from the video library."""

        if len(self.current_video) > 0 and not self.stopped:
            choice1 = random.choice(self.id_list)
            print(f'Stopping video: {self.current_video[-1]}')
            print(f'Playing video: {self.name_dict[choice1]}')
            self.current_video.append(self.name_dict[choice1])
        else:
            choice2 = random.choice(self.id_list)
            print(f'Playing video: {self.name_dict[choice2]}')
            self.current_video.append(self.name_dict[choice2])
            self.stopped = False
            self.paused = False


    def pause_video(self):
        """Pauses the current video."""

        if self.stopped or len(self.current_video) < 1:
            print('Cannot pause video: No video is currently playing')
            self.paused = True
        elif not self.stopped and len(self.current_video) > 0 and not self.paused:
            self.paused_video.append(self.current_video[-1])
            print(f'Pausing video: {self.current_video[-1]}')
            self.paused = True
        else:
            print(f'Video already paused: {self.current_video[-1]}')


    def continue_video(self):
        """Resumes playing the current video."""

        if not self.paused and not self.stopped and len(self.current_video) > 0:
            print('Cannot continue video: Video is not paused')
        elif self.stopped or len(self.current_video) < 1:
            print('Cannot continue video: No video is currently playing')
        else:
            print(f'Continuing video: {self.paused_video[-1]}')
            self.paused = False


    def show_playing(self):
        """Displays video currently playing."""

        if self.stopped or len(self.current_video) < 1:
            print('No video is currently playing')
        elif self.paused:
            v = self._video_library.get_video(self.rev_name_dict[self.paused_video[-1]])
            print(f"Currently playing: {v.title} ({v.video_id}) [{' '.join(v.tags)}] - PAUSED")
        else:
            v = self._video_library.get_video(self.rev_name_dict[self.current_video[-1]])
            print(f"Currently playing: {v.title} ({v.video_id}) [{' '.join(v.tags)}]")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self.playlist_names:
            print(f'Successfully created new playlist: {playlist_name}')
            self.playlist_names.append(playlist_name)
        else:
            print('Cannot create playlist: A playlist with the same name already exists')

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() not in self.playlist_names:
            print(f'Cannot add video to {playlist_name}: Playlist does not exist')
        elif playlist_name.lower() in self.playlist_names and (video_id not in self.id_list):
            print(f'Cannot add video to {playlist_name}: Video does not exist')
        elif playlist_name.lower() in self.playlist_names and (video_id in self.id_list):
            print(f'Added video to {playlist_name}: {self.name_dict[video_id]}')
            self.playlists[playlist_name.lower()].append(video_id)


    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.playlist_names) < 1:
            print('No playlists exist yet')
        else:
            print('Showing all playlists:')
            print(*self.playlist_names,sep='\n')
        

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self.playlist_names:
            print(f'Cannot show playlist {playlist_name}: Playlist does not exist')
        elif playlist_name.lower() in self.playlist_names and playlist_name.lower() not in list(self.playlists.keys()):
            print(f'Showing playlist: {playlist_name}')
            print('\tNo videos here yet')
        else:
            print(f'Show playlist: {playlist_name}')
            print(f'{self.playlists[playlist_name.lower()]}')
            for video_id
                 r = self._video_library.get_video(self.playlists[playlist_name.lower()])
                 print(f"\t{r.title} ({r.video_id}) [{' '.join(r.tags)}]")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

v = VideoPlayer()
v.number_of_videos()
v.show_all_videos()
v.play_video('amazing_cats_video_id')
# v.play_video('life_at_google_video_id')
# v.play_video('another_cat_video_id')
v.show_playing()
v.create_playlist('mylist')
v.create_playlist('MyLIst')
v.add_to_playlist('mylist','funny_dogs_video_id')
v.add_to_playlist('mylist','funy_dogs_video_id')
v.create_playlist('sicklist')
v.create_playlist('bestplaylist')
v.show_all_playlists()
v.add_to_playlist('mylist','life_at_google_video_id')
v.show_playlist('sicklist')
v.show_playlist('mylist')