import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {TopicDetailComponent} from './topic-detail.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [
    TopicDetailComponent
  ],
  exports: [
    TopicDetailComponent
  ]
})
export class TopicDetailModule { }
