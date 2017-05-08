import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ReplyBoxComponent} from './reply-box.component';
import {FormsModule} from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,
    FormsModule
  ],
  declarations: [
    ReplyBoxComponent
  ],
  exports: [
    ReplyBoxComponent
  ]
})
export class ReplyBoxModule { }
