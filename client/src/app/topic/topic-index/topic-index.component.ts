import { Component, OnInit } from '@angular/core';
import {Topic} from '../topic/topic';
import {TopicService} from '../topic/topic.service';
import {forEach} from '@angular/router/src/utils/collection';

@Component({
  moduleId: module.id,
  selector: 'app-topic-index',
  templateUrl: 'topic-index.component.html',
  styleUrls: ['topic-index.component.css']
})
export class TopicIndexComponent implements OnInit {
  topics: Topic[];

  constructor(private topicService: TopicService) { }

  ngOnInit() {
    this.topicService.getAll()
      .then(res => this.topics = res);
  }
}
