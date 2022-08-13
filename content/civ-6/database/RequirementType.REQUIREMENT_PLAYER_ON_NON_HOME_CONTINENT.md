---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_ON_NON_HOME_CONTINENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_ON_NON_HOME_CONTINENT
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_ON_NEW_CONTINENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_ON_NEW_CONTINENT",
		"REQUIREMENT_PLAYER_ON_NON_HOME_CONTINENT"
	);

```
