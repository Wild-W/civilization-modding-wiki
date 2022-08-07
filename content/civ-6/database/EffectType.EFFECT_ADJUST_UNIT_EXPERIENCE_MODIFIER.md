---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_EXPERIENCE_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_EXPERIENCE_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GREATPERSON_GENGHIS_KHAN_ACTIVE_UNIT_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GENGHIS_KHAN_ACTIVE_UNIT_BONUS",
		"MODIFIER_PLAYER_UNIT_ADJUST_UNIT_EXPERIENCE_MODIFIER",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_GENGHIS_KHAN_ACTIVE_UNIT_BONUS",
		"Amount",
		25
	);
	
```

