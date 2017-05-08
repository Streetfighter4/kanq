import { Component } from '@angular/core';
import {PaginatedListComponent} from '../../paginated-list/paginated-list.component';
import {Topic} from '../topic/topic';
import {TopicService} from '../topic/topic.service';

@Component({
  moduleId: module.id,
  selector: 'topic-index',
  templateUrl: 'topic-index.component.html',
  styleUrls: ['topic-index.component.css']
})
export class TopicIndexComponent extends PaginatedListComponent<Topic> {
  constructor(private topicService: TopicService) {
    super();
  }

  loadNextPage(currentPage: number, perPage: number) {
    this.topicService.getAll(currentPage, perPage)
      .then(this.addPage.bind(this));
  }
}
