import {Component, OnInit} from '@angular/core';
import {PostService} from '../post/post.service';
import {Post} from '../post/post';
import {PaginatedListComponent} from '../paginated-list/paginated-list.component';

@Component({
  moduleId: module.id,
  templateUrl: 'feed.component.html'
})
export class FeedComponent extends PaginatedListComponent<Post> {
  constructor(private postService: PostService) {
    super();
  }

  loadNextPage(perPage: number, currentPage: number) {
    this.postService.getFeed(currentPage, perPage)
      .then(res => this.addPage(res));
  }
}
