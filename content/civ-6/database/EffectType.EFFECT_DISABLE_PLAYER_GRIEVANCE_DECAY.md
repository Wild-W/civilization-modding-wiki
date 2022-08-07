---
tags:
- EffectType
title: EFFECT_DISABLE_PLAYER_GRIEVANCE_DECAY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DISABLE_PLAYER_GRIEVANCE_DECAY
>
> * Class: `Unknown`
> * Parameters:
>	* Disable `Boolean`

## Samples

```SQL {title="CYBER_WARFARE_DISABLE_GRIEVANCE_DECAY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CYBER_WARFARE_DISABLE_GRIEVANCE_DECAY",
		"MODIFIER_PLAYER_DISABLE_GRIEVANCE_DECAY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CYBER_WARFARE_DISABLE_GRIEVANCE_DECAY",
		"Disable",
		1
	);
	
```

