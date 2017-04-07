import { Component, OnInit } from '@angular/core';
import {Topic} from '../topic/topic';

@Component({
  moduleId: module.id,
  selector: 'topic-index',
  templateUrl: 'topic-index.component.html',
  styleUrls: ['topic-index.component.css']
})
export class TopicIndexComponent implements OnInit {
  topics: Topic[];

  constructor() { }

  ngOnInit() {

  }
}
