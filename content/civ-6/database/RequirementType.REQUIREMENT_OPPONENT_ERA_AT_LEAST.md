---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_ERA_AT_LEAST
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_ERA_AT_LEAST
>
> * Class: `UNITS`
> * Arguments:
>	* MinimumEraType `String`
>		* [Eras.EraType]

## Samples

```SQL {title="OPPONENT_INFO_FUTURE_ERA"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"OPPONENT_INFO_FUTURE_ERA",
		"REQUIREMENT_OPPONENT_ERA_AT_LEAST"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"OPPONENT_INFO_FUTURE_ERA",
		"MinimumEraType",
		"ERA_INFORMATION"
	);
	
```
