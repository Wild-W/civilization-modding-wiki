---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_SHARES_HOME_CONTINENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_SHARES_HOME_CONTINENT
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_SAME_HOME_CONTINENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_SAME_HOME_CONTINENT",
		"REQUIREMENT_PLAYER_SHARES_HOME_CONTINENT"
	);


```
