import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Topic} from '../topic/topic';
import {PaginatedListComponent} from '../../paginated-list/paginated-list.component';
import {Post} from '../../post/post';
import {PostService} from '../../post/post.service';
import {TopicService} from '../topic/topic.service';

@Component({
  selector: 'app-topic-new',
  templateUrl: './topic-new.component.html',
  styleUrls: ['./topic-new.component.css']
})
export class TopicNewComponent extends PaginatedListComponent<Post> {
  id: number;
  topic: Topic;

  constructor(private route: ActivatedRoute,
              private postService: PostService,
              private topicService: TopicService) {
    super();
  }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.id = +params['id'];
      this.topicService.getDetail(this.id)
        .then(res => this.topic = res);
    });

    super.ngOnInit();
  }

  loadNextPage(currentPage: number, perPage: number) {
    this.postService.getNew(currentPage, perPage, this.id)
      .then(res => this.addPage(res));
  }
}
