---
tags:
- RequirementType
title: REQUIREMENT_GREAT_PERSON_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GREAT_PERSON_TYPE_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* GreatPersonClassType `String`
>		* [GreatPersonClasses.GreatPersonClassType]

## Samples

```SQL {title="REQUIREMENT_UNIT_IS_ADMIRAL"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_UNIT_IS_ADMIRAL",
		"REQUIREMENT_GREAT_PERSON_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_UNIT_IS_ADMIRAL",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_ADMIRAL"
	);
	
```
