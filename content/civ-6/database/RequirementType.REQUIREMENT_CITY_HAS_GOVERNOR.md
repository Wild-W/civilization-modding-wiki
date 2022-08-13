---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_GOVERNOR
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_GOVERNOR
>
> * Class: `CITIES`
> * Arguments:
>	* Established `Boolean`

## Samples

```SQL {title="REQUIRES_CITY_HAS_GOVERNOR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_GOVERNOR",
		"REQUIREMENT_CITY_HAS_GOVERNOR"
	);

```

```SQL {title="REQUIRES_CITY_WITH_ASSIGNED_GOVERNOR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_WITH_ASSIGNED_GOVERNOR",
		"REQUIREMENT_CITY_HAS_GOVERNOR"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_WITH_ASSIGNED_GOVERNOR",
		"Established",
		0
	);
	```
