import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'error_fields'
})
export class ErrorFieldsPipe implements PipeTransform {

  transform(value: any, args: string[]): any {
    let keys = [];

    for(let key in value) {
      keys.push({name: key, errors: value[key]});
    }

    return keys;
  }
}
