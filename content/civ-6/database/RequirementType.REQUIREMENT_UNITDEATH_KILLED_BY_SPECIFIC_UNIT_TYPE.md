---
tags:
- RequirementType
title: REQUIREMENT_UNITDEATH_KILLED_BY_SPECIFIC_UNIT_TYPE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNITDEATH_KILLED_BY_SPECIFIC_UNIT_TYPE
>
> * Class: `Unknown`
> * Arguments:
>	* UnitType `Unknown`

## Samples

```SQL {title="KILLED_BY_ZOMBIE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"KILLED_BY_ZOMBIE",
		"REQUIREMENT_UNITDEATH_KILLED_BY_SPECIFIC_UNIT_TYPE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"KILLED_BY_ZOMBIE",
		"UnitType",
		"UNIT_MODE_ZOMBIE"
	);
	
```