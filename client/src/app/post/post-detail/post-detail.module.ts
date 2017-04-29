import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {PostDetailComponent} from './post-detail.component';
import {PostService} from '../post.service';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [
    PostDetailComponent
  ],
  exports: [
    PostDetailComponent
  ],
  providers: [
    PostService
  ]
})
export class PostDetailModule { }
