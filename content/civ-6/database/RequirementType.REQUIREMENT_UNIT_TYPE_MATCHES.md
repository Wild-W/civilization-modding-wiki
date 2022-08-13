---
tags:
- RequirementType
title: REQUIREMENT_UNIT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_TYPE_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* UnitType `String`
>		* [Units.UnitType]

## Samples

```SQL {title="REQUIREMENT_UNIT_IS_BUILDER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_UNIT_IS_BUILDER",
		"REQUIREMENT_UNIT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_UNIT_IS_BUILDER",
		"UnitType",
		"UNIT_BUILDER"
	);
	```
