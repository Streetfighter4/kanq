import {Component, OnInit} from '@angular/core';
import {Topic} from '../topic';
import {TopicService} from '../topic.service';
import {PaginatedListComponent} from '../../paginated-list/paginated-list.component';

@Component({
  moduleId: module.id,
  selector: 'app-topic-index',
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
