---
tags:
- RequirementType
title: REQUIREMENT_UNIT_ON_HOME_CONTINENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_ON_HOME_CONTINENT
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="NOT_OWNER_CAPITAL_CONTINENT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"NOT_OWNER_CAPITAL_CONTINENT_REQUIREMENT",
		"REQUIREMENT_UNIT_ON_HOME_CONTINENT",
		1
	);


```
