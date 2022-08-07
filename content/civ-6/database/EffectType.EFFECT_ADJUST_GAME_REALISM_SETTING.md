---
tags:
- EffectType
title: EFFECT_ADJUST_GAME_REALISM_SETTING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GAME_REALISM_SETTING
>
> * Class: `Unknown`
> * Parameters:
>	* RealismSettingType `String`
>		* [RealismSettings.RealismSettingType]

## Samples
```SQL {title="MEGADISASTERS_MODE_SET_REALISM_TO_MEGADISASTERS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MEGADISASTERS_MODE_SET_REALISM_TO_MEGADISASTERS",
		"MODIFIER_GAME_SET_REALISM_SETTING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MEGADISASTERS_MODE_SET_REALISM_TO_MEGADISASTERS",
		"RealismSettingType",
		"REALISM_SETTING_MEGADISASTERS"
	);
	
```

