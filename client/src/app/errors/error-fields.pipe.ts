import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'error_fields'
})
export class ErrorFieldsPipe implements PipeTransform {

  transform(value: any, args: string[]): any {
    let keys = [];

    console.log('Value', value);

    for(let key in value) {
      // We only want the field errors
      if(key != 'non_field_errors') {
        keys.push({name: key, errors: value[key]});
      }
    }

    console.log('Keys', keys);
    return keys;
  }
}
