---
tags:
- RequirementType
title: REQUIREMENT_UNIT_ON_COAST
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_ON_COAST
>
> * Class: `UNITS`
> * Arguments:
>	* Water `Boolean`

## Samples

```SQL {title="REQUIRES_UNIT_IN_SHALLOW_WATER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_UNIT_IN_SHALLOW_WATER",
		"REQUIREMENT_UNIT_ON_COAST"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_UNIT_IN_SHALLOW_WATER",
		"Water",
		1
	);
	```
